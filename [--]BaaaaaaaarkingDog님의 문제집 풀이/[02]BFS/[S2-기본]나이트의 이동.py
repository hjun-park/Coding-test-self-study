import sys
from collections import deque

input = sys.stdin.readline

moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

q = deque()


def bfs(go, to):
    start_x, start_y = go[0], go[1]
    q = deque()
    q.append((start_x, start_y))
    graph[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        if x == to[0] and y == to[1]:
            return graph[x][y]

        for m in moves:
            nx = x + m[0]
            ny = y + m[1]

            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == -1:  # 이동한 적이 없다면
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


for _ in range(int(input().rstrip())):
    l = int(input().rstrip())
    graph = [[-1] * l for _ in range(l)]

    go = list(map(int, input().split()))
    to = list(map(int, input().split()))

    # visited = [[-1] * l for _ in range(l)]
    print(bfs(go, to))
