import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

'''
    턴 1번은 1번부터 K번 말까지 순서대로 돈다.
    종료: 말이 4개 이상 쌓이는 순간 게임 종료
'''


def turn_direction(d):
    if d == 0:
        return 1

    elif d == 1:
        return 0

    elif d == 2:
        return 3

    elif d == 3:
        return 2


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
    _map[x - 1][y - 1].append([i, d - 1])


def move_white(x, y, nx, ny):
    global _map

    # 이동하려는 칸에 말이 있는 경우 -> 그 뒤로 추가
    while _map[x][y]:
        _map[nx][ny].append(_map[x][y].popleft())


def move_red(x, y, nx, ny):
    global _map

    # reverse 후 이동
    # _map[x][y].reverse()
    # _map[nx][ny].append(_map[x][y][:-1])
    # _map[x][y] = []
    while _map[x][y]:
        _map[nx][ny].append(_map[x][y].pop())


# 방향을 바꾸고 이동 (근데 이동하는 곳이 파란색이라면 이동 금지)
# red와 white와는 다르게 가장 먼저 있는 말 혼자 이동한다는 것이 특징
def move_blue(x, y, nx, ny):
    global _map

    # 방향 바꾸어 이동하려는 곳이 파란색 or 벼랑 경우 이동하지 않음
    # if 0 <= nx < N and 0 <= ny < N:

    if not (0 <= nx < N and 0 <= ny < N):
        return

    if graph[nx][ny] == 2:
        return

    # 한 칸 이동
    # while _map[x][y]:
    #     _map[nx][ny].append(_map[x][y].popleft())
    _map[nx][ny].append(_map[x][y].popleft())

    # 2번째 말

    # _map[x][y].clear()

turn = 0
while True:
    turn += 1
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

                        if 0 <= ni < N and 0 <= nj < N:
                            # 이동하려는 곳의 색 확인
                            if graph[ni][nj] == 0:  # 흰색
                                move_white(i, j, ni, nj)

                            elif graph[ni][nj] == 1:  # 빨간
                                move_red(i, j, ni, nj)

                            elif graph[ni][nj] == 2:  # 파랑
                                # 이동방향 반대로 변경
                                _map[i][j][0][1] = turn_direction(_map[i][j][0][1])

                                ni = i + dx[_map[i][j][0][1]]
                                nj = j + dy[_map[i][j][0][1]]

                                move_blue(i, j, ni, nj)

                        else:  # 이동범위를 벗어난 경우 파란색
                            # 이동방향 반대로 변경
                            _map[i][j][0][1] = turn_direction(_map[i][j][0][1])
                            # _map[i][j][0][1] = (_map[i][j][0][1] + 2) % 4

                            ni = i + dx[_map[i][j][0][1]]
                            nj = j + dy[_map[i][j][0][1]]

                            move_blue(i, j, ni, nj)

                        # 말 이동 후 4개 쌓여있나 체크
                        for i in range(N):
                            for j in range(N):
                                if len(_map[i][j]) >= 4:
                                    print(turn)
                                    sys.exit(0)

                        if turn >= 1000:
                            print(-1)
                            sys.exit(0)

