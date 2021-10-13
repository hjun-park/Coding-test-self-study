import sys
from collections import deque

input = sys.stdin.readline

'''
    참고: https://jeongchul.tistory.com/666
    -> 회전과 탐색 두 가지를 분리하여 구현
'''

N, M = map(int, input().split())
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
graph = [list(input().rstrip()) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

rx, ry, bx, by = [0] * 4
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'B':
            bx, by = i, j
        elif graph[i][j] == 'R':
            rx, ry = i, j


def tilt(x, y, dx, dy):
    count = 0
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1

    return x, y, count


def bfs():
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

    while q:
        qrx, qry, qbx, qby, depth = q.popleft()
        # 검증
        if depth > 10:
            break

        for d in range(4):
            next_rx, next_ry, r_count = tilt(qrx, qry, dx[d], dy[d])
            next_bx, next_by, b_count = tilt(qbx, qby, dx[d], dy[d])

            if graph[next_bx][next_by] == 'O':
                continue

            if graph[next_rx][next_ry] == 'O':
                print(depth)
                return

            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx -= dx[d]
                    next_ry -= dy[d]
                else:
                    next_bx -= dx[d]
                    next_by -= dy[d]

            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth + 1))

    print(-1)


bfs()
