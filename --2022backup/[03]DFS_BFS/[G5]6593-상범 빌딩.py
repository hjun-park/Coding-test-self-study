import sys
from collections import deque

input = sys.stdin.readline

# 위 좌 상 우 하 아래
dz = [1, 0, 0, 0, 0, -1]
dx = [0, 0, -1, 0, 1, 0]
dy = [0, -1, 0, 1, 0, 0]


def bfs(start_z, start_x, start_y):
    q = deque()
    q.append((start_z, start_x, start_y))
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    visited[start_z][start_x][start_y] = 0

    while q:
        z, x, y = q.popleft()

        if building[z][x][y] == 'E':
            return visited[z][x][y]

        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if building[nz][nx][ny] != '#' and visited[nz][nx][ny] == -1:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append((nz, nx, ny))

    return -1


def find_start(building: list):
    for z in range(L):
        for x in range(R):
            for y in range(C):
                if building[z][x][y] == 'S':
                    return z, x, y


while True:
    # Line, row, column
    L, R, C = map(int, input().split())

    if (L, R, C) == (0, 0, 0):
        sys.exit(0)

    building = []
    for _ in range(L):
        building.append([list(input().rstrip()) for _ in range(R)])
        input().rstrip()

    start_z, start_x, start_y = find_start(building)
    minute = bfs(start_z, start_x, start_y)

    if minute != -1:
        print(f'Escaped in {minute} minute(s).')
    else:
        print('Trapped!')
