import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    cnt_arr = [[0] * M for _ in range(N)]
    cnt_arr[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 'x' and not cnt_arr[nx][ny]:
                    cnt_arr[nx][ny] = cnt_arr[x][y] + 1
                    q.append([nx, ny])
    return cnt_arr


while True:
    M, N = map(int, input().split())

    if M == 0 and N == 0:
        break

    nx, ny = 0, 0
    graph, dusts = [], []

    for i in range(N):
        row = list(input().strip())
        graph.append(row)
        for j, k in enumerate(row):
            if k == 'o':
                nx, ny = i, j
            elif k == '*':
                dusts.append([i, j])

    vt_d, dusts_all = [], True
    moves = bfs(nx, ny)

    for i, j in dusts:
        if not moves[i][j]:
            dusts_all = False
            break
        vt_d.append(moves[i][j] - 1)

    if not dusts_all:
        print(-1)
        continue

    dust_to_dust = [[0] * len(dusts) for _ in range(len(dusts))]

    for i in range(len(dusts) - 1):
        moves = bfs(dusts[i][0], dusts[i][1])
        for j in range(i + 1, len(dusts)):
            dust_to_dust[i][j] = moves[dusts[j][0]][dusts[j][1]] - 1
            dust_to_dust[j][i] = dust_to_dust[i][j]

    rst = sys.maxsize
    t = False
    for pm in list(permutations([x for x in range(len(dust_to_dust))])):
        d = 0
        d += vt_d[pm[0]]
        dust_start = pm[0]

        for j in range(1, len(pm)):
            dust_to = pm[j]
            d += dust_to_dust[dust_start][dust_to]
            dust_start = dust_to
        rst = min(rst, d)
    print(rst)
