import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
melted_graph = [[0] * M for _ in range(N)]

# 구현
# 1) 얼음 덩어리가 몇 개인지 확인
# 2) 1년 후 빙하가 녹은 것 계산

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 2) 1년 후 빙하가 녹은 것 계산
def melt(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if graph[nx][ny] > 0:
            graph[nx][ny] -= 1

    return 1


def melt_v2():
    print(f'melted_graph {melted_graph}')
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                graph[i][j] -= melted_graph[i][j]

    print(graph)


def melt_v3(*graphs):
    return [[row[0] * 2 - sum(row) for row in zip(*t)] for t in zip(*graphs)]


# BFS 돌면서 0이 몇 개인지 따로 기록
def bfs(x, y):
    is_visit = False
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        qx, qy = q.popleft()

        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] != 0:
                    is_visit = True
                    visited[nx][ny] = True
                    q.append((nx, ny))

                if graph[nx][ny] == 0: # and melted_graph[qx][qy] < graph[qx][qy]:
                    melted_graph[qx][qy] += 1

    if is_visit:
        return 1
    else:
        return 0


# 1)
count = 0
year = 0
melted = 0

while True:
    visited = [[False] * M for _ in range(N)]
    # 빙하 개수 세기
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                count += bfs(i, j)  # 빙하 개수 세기
                print(count)

            if count > 1:  # 빙하 개수가 2개 이상이라면
                print(f'year is {year}')
                sys.exit(0)

    # 빙하가 없는 경우
    if count <= 0:
        print(f'nothing melt {0}')
        sys.exit(0)

    # # 빙하가 녹는 경우
    # for i in range(N):
    #     for j in range(M):
    #         if graph[i][j] > 0:
    #             melted += melt(i, j)

    melt_v2()

    year += 1
