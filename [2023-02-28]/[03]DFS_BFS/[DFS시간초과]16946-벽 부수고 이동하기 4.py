import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = [[0] * M for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

count = 1


def dfs(x, y):
    global count
    # visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                dfs(nx, ny)
                count += 1


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = 0
            visited[i][j] = True
            dfs(i, j)
            result[i][j] = count % 10
            visited = [[False] * M for _ in range(N)]
            count = 1
            graph[i][j] = 1

for i in range(N):
    print(*result[i])
