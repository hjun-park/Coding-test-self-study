import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

'''
    전형적인 BFS 문제 (기본)
'''

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
