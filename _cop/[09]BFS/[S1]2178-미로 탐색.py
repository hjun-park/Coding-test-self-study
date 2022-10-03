import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


def bfs(a, b):
    q = deque()
    q.append([a, b, 1])
    visited[a][b] = True

    while q:
        x, y, cnt = q.popleft()

        if x == N - 1 and y == M - 1:
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt + 1])


print(bfs(0, 0))
