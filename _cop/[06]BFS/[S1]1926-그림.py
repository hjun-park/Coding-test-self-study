import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

_max = -1
pic_count = 0
visited = [[0] * m for _ in range(n)]


def bfs(a, b):
    visited[a][b] = 1
    q = deque()
    q.append([a, b])
    depth = 1  # 이미 1인 지점부터 시작하므로 넓이는 1부터 시작

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    depth += 1
                    q.append([nx, ny])
    return depth


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            pic_count += 1
            _cnt = bfs(i, j)
            _max = max(_max, _cnt)

if pic_count == 0:
    print(0)
    print(0)
else:
    print(pic_count)
    print(_max)
