import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

'''
    턴 1번은 1번부터 K번 말까지 순서대로 돈다.
    종료: 말이 4개 이상 쌓이는 순간 게임 종료
'''

# 체스 크기 / 말의 개수
N, K = map(int, input().split())

# 0: 흰색 / 1: 빨간색 / 2: 파란색
graph = [list(map(int, input().split())) for _ in range(N)]

# 말의 이동방향
_map = [[deque() for _ in range(N)] for _ in range(N)]

# 말의 정보 (1번부터 K번까지)
# info = []

# 말의 정보 (행/열/이동방향)
for i in range(K):
    x, y, d = map(int, input().split())
    _map[x - 1][y - 1].append((i, d))


def move_white(x, y, nx, ny):
    global _map

    # 이동하려는 칸에 말이 있는 경우 -> 그 뒤로 추가
    # if _map[nx][ny][0][0]:
    _map[nx][ny].extend(_map[x][y])
    _map[x][y].clear()
    # 이동하려는 칸에 말이 없는 경우 그냥 추가
    # else:


def move_red(x, y):
    pass


def move_blue(x, y):
    pass


while True:
    # 1번말부터 K번까지 1회 이동 시작
    for k in range(K):
        for i in range(N):
            for j in range(N):
                # q의 첫 번째 요소가 k인 말을 찾음
                if _map[i][j]:
                    if _map[i][j][0][0] == k:
                        # 그래프에 따라 말을 이동
                        ni = i + dx[_map[i][j][0][1]]
                        nj = j + dy[_map[i][j][0][1]]

                        if graph[ni][nj] == 0:  # 흰색
                            move_white(i, j, ni, nj)
                            # pass
                            sys.exit(0)
                        elif graph[ni][nj] == 1:  # 빨간
                            move_red(ni, nj)
                            pass
                        elif graph[ni][nj] == 2:  # 파랑
                            move_blue(ni, nj)
                            pass

    break
