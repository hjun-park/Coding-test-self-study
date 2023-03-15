import sys
from collections import deque

input = sys.stdin.readline

'''

board: 체스판 칸 색깔
graph: 각 칸에 어떤 말들이 있는지 나타냄
chess: 체스 말들의 위치와 방향정보

    [이동좌표]
    - 흰색: 정상이동, 이동지역에 말이 있는 경우 append (업는다)
    - 빨간색: reverse 후 이동, 이동지역에 말이 있는 경우 append (업는다)
    - 파란색 or 막힘 : 반대방향 한 칸 이동 (반대방향 이동 시에 반대방향이 빨/파/흰일 수도 있으니 이걸 고려해야 한다)
    
    [이동 후]
    - 만약 4개의 말이 겹쳐있다면 바로 턴을 출력해주고 종료시켜준다.
    - 1000번이 지나도록 출력이 되지 않았다면 -1을 출력해준다.

'''


def check(nx, ny):
    if len(graph[nx][ny]) >= 4:
        return True
    return False


def move_white(x, y, nx, ny):
    # print(f'이동 전 {graph[x][y]} -> {graph[nx][ny]}')
    # 흰색: 정상이동, 이동지역에 말이 있는 경우 append (업는다)
    first = graph[x][y].index(j)    # j번째 말을 시작점
    last = len(graph[x][y])         # 끝번째 말을 종료점

    # 한 좌표에 있는 여러 말의 정보를 순환하며 좌표정보를 수정
    for k in range(first, last):  # k = 한 좌표에 있는 여러 말 중 하나
        chess[graph[x][y][k]][0] = nx
        chess[graph[x][y][k]][1] = ny
        graph[nx][ny].append(graph[x][y][k])

    for _ in range(first, last):
        graph[x][y].pop()

    # for k in range(len(graph[x][y])):
    #     chess[graph[x][y][k]][0] = nx
    #     chess[graph[x][y][k]][1] = ny
    #     graph[nx][ny].append(graph[x][y].popleft())

    # print(f'이동 후 {graph[x][y]} -> {graph[nx][ny]}')
    # print()


def move_red(x, y, nx, ny):
    # print(f'red = {graph[x][y]}')
    # 빨간색: reverse 후 이동, 이동지역에 말이 있는 경우 append (업는다)
    first = graph[x][y].index(j)
    last = len(graph[x][y])

    for k in range(last - 1, first - 1, - 1):
        chess[graph[x][y][k]][0] = nx
        chess[graph[x][y][k]][1] = ny
        graph[nx][ny].append(graph[x][y][k])

    for _ in range(first, last):
        graph[x][y].pop()


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]  # 체스 보드판 정보
chess = []  # 체스말의 방향정보
graph = [[deque() for _ in range(N)] for _ in range(N)]  # 체스 말 쌓여있는 정보

# 1번 말 부터 K번 말 까지 순회하면서 정보 반영
for i in range(K):
    x, y, d = map(int, input().split())
    graph[x - 1][y - 1].append(i)  # 체스 좌표에 추가
    chess.append([x - 1, y - 1, d])  # 말 순서대로 정보를 집어 넣음

# 1000번을 넘어서면 종료되도록 설정
for i in range(1, 1001):
    # 1번 말부터 순회 시작
    for j in range(K):
        x, y, d = chess[j]

        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 내면서 보드판이 0인 경우 white 동작
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
            move_white(x, y, nx, ny)

            # 말을 이동했을 때 4층 이상 쌓였는지 확인
            if check(nx, ny):
                print(i)
                exit()

        # 범위 내면서 보드판이 1인 경우 red 동작
        elif 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
            move_red(x, y, nx, ny)

            # 말을 이동했을 때 4층 이상 쌓였는지 확인
            if check(nx, ny):
                print(i)
                exit()

        # 범위를 벗어나거나 보드판이 2인 경우 blue 동작
        elif not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:

            # 방향 반대로 변경
            if d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 4
            elif d == 4:
                d = 3

            # 현재 말의 방향 정보를 d로 변경
            chess[j][2] = d

            # 변경된 방향 정보 기준으로 진행방향 수정
            nx = x + dx[d]
            ny = y + dy[d]

            # 변경된 진행방향이 흰색인 경우
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                move_white(x, y, nx, ny)

                # 말을 이동했을 때 4층 이상 쌓였는지 확인
                if check(nx, ny):
                    print(i)
                    exit()

            elif 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
                move_red(x, y, nx, ny)

                # 말을 이동했을 때 4층 이상 쌓였는지 확인
                if check(nx, ny):
                    print(i)
                    exit()

            # 변경된 진행방향이 파란색인 경우 => 그대로 있음
            else:
                continue
else:  # for문이 끝나면 1000번이 실행된 것이므로 -1 출력
    print(-1)
