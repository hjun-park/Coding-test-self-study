import sys
from collections import deque

sys.setrecursionlimit(10000)

def bfs(x, y):
    count = 1
    # deque 생성 후 넣고 시작
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
    return count

# https://www.acmicpc.net/problem/1926
# output : 총 그림 개수, 가장 큰 면적 그림 사이즈

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
max_size = 0
count = 0

# 좌 상 우 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        # 조건 걸어주기
        if graph[i][j] == 1 and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))
            count += 1

print(count)
print(max_size)
