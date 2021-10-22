import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    current_color = graph[x][y]

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == current_color:
                    visited[nx][ny] = True
                    q.append((nx, ny))


three_color = 0
two_color = 0
# 일반인 관점
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
            three_color += 1

# Green -> Red
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * N for _ in range(N)]

# 색약인 관점
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
            two_color += 1

print(three_color, two_color)
