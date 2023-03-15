import sys
from collections import deque

input = sys.stdin.readline

L, W = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(L)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# one -> 1H

max_depth = 0


def bfs(a, b):
    global max_depth
    visited[a][b] = True
    depth = 0

    q = deque()
    q.append((a, b, depth))

    while q:
        x, y, depth = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < L and 0 <= ny < W:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, depth + 1))

        max_depth = max(depth, max_depth)


path = 0
for i in range(L):
    for j in range(W):
        if graph[i][j] == 'L':
            visited = [[False] * W for _ in range(L)]
            bfs(i, j)

print(max_depth)
