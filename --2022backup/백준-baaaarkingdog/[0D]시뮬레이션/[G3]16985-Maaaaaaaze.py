import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

graph = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

_map = [[[0] * 5 for _ in range(5)] for _ in range(5)]

dx = [0, 0, -1, 0, 1, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [1, 0, 0, 0, 0, -1]

time = []

def bfs():
    q = deque()
    q.append((0, 0, 0))

    visited = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0

    while q:
        z, x, y = q.popleft()

        # exit
        if z == 4 and x == 4 and y == 4:
            time.append(visited[z][x][y])
            return

        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nz][nx][ny] == -1 and _map[nz][nx][ny] == 1:
                    q.append((nz, nx, ny))
                    visited[nz][nx][ny] = visited[z][x][y] + 1


def recursion_log(layer):
    if layer == 5:
        if _map[4][4][4]:
            bfs()
        return

    for r in range(4):
        if _map[0][0][0]:
            recursion_log(layer + 1)

        tmp = [[0] * 5 for _ in range(5)]

        for j in range(5):
            for k in range(5):
                tmp[k][4 - j] = _map[layer][j][k]
        _map[layer] = tmp


for p in permutations([0, 1, 2, 3, 4]):
    for i in range(5):
        _map[p[i]] = graph[i]

    recursion_log(0)

print(min(time) if time else -1)
