import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# bfs 안 쓰고 반복문으로 해결
def melt_ice(graph):
    copied_graph = deepcopy(graph)

    for x in range(N):
        for y in range(M):
            zero_cnt = 0
            if graph[x][y] > 0:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == 0:
                            zero_cnt += 1

                # 하나에 대해서 루프가 끝났으니 값 계산
                if graph[x][y] - zero_cnt <= 0:
                    copied_graph[x][y] = 0
                elif graph[x][y] - zero_cnt > 0:
                    copied_graph[x][y] = graph[x][y] - zero_cnt

    return copied_graph


def count_ice(a, b):
    q = deque()
    visited[a][b] = True
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and melted_graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))


year = 0
while True:
    year += 1
    visited = [[False] * M for _ in range(N)]

    melted_graph = melt_ice(graph)

    count = 0
    # 덩어리 개수를 셀 차례
    for i in range(N):
        for j in range(M):
            if melted_graph[i][j] > 0 and not visited[i][j]:
                count_ice(i, j)
                count += 1

    graph = deepcopy(melted_graph)

    if count > 1:
        print(year)
        break
    elif count == 0:  # 분리가 안 된다면
        print(0)
        break
