import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(start_x, start_y, crash):
    q = deque()
    q.append((start_x, start_y, crash))
    visited[start_x][start_y][crash] = 1

    while q:
        x, y, crash = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][crash]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽을 부수지 않는 경우
            if graph[nx][ny] == 0 and visited[nx][ny][crash] == 0:
                q.append((nx, ny, crash))
                visited[nx][ny][crash] = visited[x][y][crash] + 1

            # 벽을 부수는 경우
            # crash <= K 를 하게되면 범위 문제
            if graph[nx][ny] == 1 and crash < K:
                q.append((nx, ny, crash+1))
                visited[nx][ny][crash+1] = visited[x][y][crash] + 1

    return -1


print(bfs(0, 0, 0))
