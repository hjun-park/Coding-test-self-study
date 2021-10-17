from collections import deque
import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

year = 0  # 년도


# 1년 후의 빙산 형태로 반환
def after_iceberg(graph):  # 섬의 숫자 줄이기
    copy_graph = copy.deepcopy(graph)

    for x in range(0, N):
        for y in range(0, M):
            zero_zone = 0
            if graph[x][y] > 0:     # 빙산 값이 있는 경우 4방향 체크하여 비어있는 부분 확인
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == 0:
                            zero_zone += 1

                if graph[x][y] - zero_zone <= 0:    # 빙산은 음수의 경우 0로 치환
                    copy_graph[x][y] = 0
                elif graph[x][y] - zero_zone > 0:   # 아닌 경우 그냥 뺸 값으로 저장
                    copy_graph[x][y] = graph[x][y] - zero_zone
    return copy_graph


# 섬의 개수를 세는 함수
def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and after_graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))


while True:
    year += 1
    iceberg_cnt = 0
    visited = [[False] * M for _ in range(N)]  # 방문여부

    # 1년 후 녹은 빙산
    after_graph = after_iceberg(graph)

    # bfs를 이용하여 빙산의 개수를 셈
    for i in range(0, N):
        for j in range(0, M):
            if after_graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                iceberg_cnt += 1

    graph = copy.deepcopy(after_graph)
    if iceberg_cnt >= 2:
        print(year)
        break
    elif iceberg_cnt == 0:  # 만일 빙산이 다 녹을 때까지 분리되지 않으면
        print(0)
        break

