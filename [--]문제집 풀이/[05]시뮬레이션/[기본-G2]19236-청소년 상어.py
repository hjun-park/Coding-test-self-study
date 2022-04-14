import sys
from copy import deepcopy

input = sys.stdin.readline

'''
참고 : https://developer-ellen.tistory.com/68
'''

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

board = [[] for _ in range(4)]  # 물고기의 번호, 방향정보 저장
max_score = 0

# 입력값이 너무 복잡하여 평탄화 작업
for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2 * j], data[2 * j + 1] - 1])
    board[i] = fish


# 상어 이동은 백트래킹으로 구현
def dfs(sx, sy, score, board):
    global max_score
    # 1) 상어가 해당 sx, sy 좌표로 이동해서 잡아먹음 / 점수 추가 / 먹힌 좌표 0 초기화
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d + i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 3) 상어가 잡아먹을 차례
    shark_d = board[sx][sy][1]

    # 3-1) 상어가 최대 같은 방향으로 4번 이동 가능
    for m in range(1, 5):
        nx = sx + dx[shark_d] * m
        ny = sy + dy[shark_d] * m

        # 경계 내부에 있으며 물고기가 있는 경우
        if (0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
            # board를 복사 후 전달하면 dfs 복구하지 않아도 된다.
            dfs(nx, ny, score, deepcopy(board))


dfs(0, 0, 0, board)
print(max_score)
