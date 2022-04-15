import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

'''

 [참고] https://dirmathfl.tistory.com/386?category=825041

 - 상어의 위치와 상어의 방향이 주어진다.
 - 이때 각 상어들은 이동하며 냄새를 뿌린다.
 - 뿌려진 냄새는 K초가 지나면 사라진다.

 - 이는 간단하게 생각하면
   1) 냄새 뿌리기, 2) 상어 이동, 3) 시간에 따른 냄새 감소로 나누어 그대로 구현하면 된다.

 - 상어의 냄새는 2차원 배열로 관리 (board)
 - 상어의 번호, 방향정보는 리스트로 관리 (sharks)
'''

# 인덱스가 헷갈리니까 상어 인덱스는 0, 냄새 인덱스는 1로 설정
SHARK, SCENT = 0, 1


def simulation():
    # 3) 자신의 자리에 냄새 뿌리기
    # - sharks 리스트 순회하면서 처리, sharks에서 뽑은 값이 없으면 당연, 상어가 없는 것 continue
    for i in range(len(sharks)):
        if sharks[i] is None:
            continue

        sx, sy, _ = sharks[i]
        # 3-1) 냄새를 뿌릴 수 있는 경우 (해당자리에 냄새가 없거나 자기 자신의 냄새라면)
        # - 냄새를 뿌린다. (해당 자리를 [자기자신번호, k]로 변경)
        # - 뿌릴 수 없다면 그 자리는 자기보다 인덱스 낮은 친구가 뿌린 것이므로 퇴출된다.
        # print(board[sx][sy][SHARK])
        if board[sx][sy] is None or board[sx][sy][SHARK] == i:
            board[sx][sy] = [i, K]
        else:
            sharks[i] = None

    # 4) 상어 이동
    # - sharks 리스트 순회하면서 처리, 3에서와 마찬가지로 sharks 값이 없다면 다음 상어로
    for i in range(len(sharks)):
        if sharks[i] is None:
            continue

        sx, sy, sd = sharks[i]

        # 빈 칸으로 이동 가능한 경우 우선순위 리스트 참고하여 이동 후 상어를 갱신한다.
        for nd in priority[i][sd]:
            nx = sx + dx[nd]
            ny = sy + dy[nd]

            if (0 <= nx < N and 0 <= ny < N) and board[nx][ny] is None:
                sharks[i] = [nx, ny, nd]
                break

        # else를 도는 경우는 빈 공간이 없었단 얘기고, 이 경우 자기 자신의 냄새를 체크하고 이동한다.
        else:
            for nd in priority[i][sd]:
                nx = sx + dx[nd]
                ny = sy + dy[nd]

                if (0 <= nx < N and 0 <= ny < N) and board[nx][ny][SHARK] == i:
                    sharks[i] = [nx, ny, nd]
                    break

            # 그럼에도 불구하고 이동하지 못했다면 해당 상어는 퇴출된다.
            else:
                sharks[i] = None

    # 5) 냄새 감소
    #  - 없으면 패스, 있으면 1을 빼준다, 0이라면 None으로 변경
    for x in range(N):
        for y in range(N):
            if board[x][y] is not None:
                if board[x][y][SCENT] == 0:
                    board[x][y] = None
                else:
                    board[x][y][SCENT] -= 1


N, M, K = map(int, input().split())

# deque()로 처리하려고 했으나 그럴 필요 없이 가장 작은 번호를 가진 상어부터 처리하면 알아서 처리된다.
# 상어의 냄새에 대한 정보를 담고 있다.
# 처음에는 상어의 번호 하나만 들어가겠지만 for문을 타면서 냄새를 뿌리게 되면 [번호, 냄새]로 바뀔 얘정
board = [list(map(int, input().split())) for _ in range(N)]

# 초기에 주어지는 각 상어의 방향
cur_shark_dirs = list(map(int, input().split()))

# 상어의 위치와 방향은 따로 리스트로 관리한다.
# sharks = [x좌표, y좌표, 방향]
sharks = [0] * M

# 1) board를 순회하면서 상어가 담겨있다면 sharks 리스트에 위치와 방향 정보를 담아준다.
# 이 때 board에는 상어 번호가 1-index 형식이므로 0-index로 바꾸기 위해 1을 빼준다.
# 만약 k가 3이고 상어가 냄새를 뿌렸다면 3 -> 2 -> 1 -> 0(냄새존재) -> None(냄새없음) 순으로 감소 예정
# 그렇기 때문에 현재 board에서 0인 경우는 None으로 바꾸어 준다.
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            sharks[board[i][j] - 1] = [i, j, cur_shark_dirs[board[i][j] - 1] - 1]  # 상어 정보 추가
            board[i][j] -= 1  # board를 0-index로 변경
        # elif board[i][j] == 0:
        board[i][j] = None

# 2) 다음으로 우선순위 리스트에 대해 값을 받아준다.
priority = [[[0] for _ in range(4)] for _ in range(M)]

# 2-1) 마찬가지로 priority를 순회하며 입력 받은 리스트는 dx dy 인덱스에 맞추기 위해 1을 빼준다.
for i in range(M):
    for j in range(4):
        priority[i][j] = [x - 1 for x in list(map(int, input().split()))]

# 2-1) 셋업 과정 까지 진행했다면 1000초까지 시뮬레이션을 돌린다.
for time in range(-1, 1001):
    # 상어 1마리 체크 ( 퇴출된 상어 수 = 전체 - 1 )
    if sharks.count(None) == M - 1:
        print(time)
        sys.exit(0)
    else:
        simulation()

else:
    print(-1)

