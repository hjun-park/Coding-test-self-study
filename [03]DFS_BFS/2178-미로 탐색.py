import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(a, b):
    visited = [[False] * M for _ in range(N)]
    visited[a][b] = True
    count = 1

    q = deque()
    q.append((a, b, count))

    while q:
        x, y, cnt = q.popleft()

        if x == N - 1 and y == M - 1:
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))


print(bfs(0, 0))
