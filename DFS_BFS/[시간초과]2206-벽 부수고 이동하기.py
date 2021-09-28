import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
# 각 노드까지 걸리는 거리를 담은 배열
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(start_x, start_y, crashed):
    q = deque()
    q.append((start_x, start_y, crashed))
    visited[start_x][start_y][crashed] = 1  # 시작지도 거리계산에 포함됨

    while q:
        x, y, crashed = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][crashed]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽을 부수지 않고 이동 (이동하려는 좌표가 벽도 없으면서 최단거리도 계산 안 된 경우)
            if graph[nx][ny] == 0 and visited[nx][ny][crashed] == 0:
                q.append((nx, ny, crashed))
                visited[nx][ny][crashed] = visited[x][y][crashed] + 1

            # 벽을 부수고 이동 (이동하려는 좌표가 벽이 있으면서 아직 그 벽을 부수지 않은 경우 )
            if graph[nx][ny] == 1 and crashed == 0:
                q.append((nx, ny, crashed + 1))  # 벽을 부쉈으니 crashed 값 증가
                visited[nx][ny][crashed + 1] = visited[x][y][crashed] + 1  # 최단거리 계산
    return -1


print(bfs(0, 0, 0))
