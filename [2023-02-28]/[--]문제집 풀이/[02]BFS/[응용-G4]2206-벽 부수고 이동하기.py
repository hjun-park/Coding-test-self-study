import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 1개의 벽을 부수는 것이 가능
def bfs(start_x, start_y, is_crashed):
    q = deque()
    q.append((start_x, start_y, is_crashed))
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[start_x][start_y][is_crashed] = 1

    is_crash = False

    while q:
        x, y, crashed = q.popleft()

        # 도착 시 종료
        if x == N - 1 and y == M - 1:
            return visited[x][y][crashed]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                # 벽을 부수지 않고 이동
                if visited[nx][ny][crashed] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][crashed] = visited[x][y][crashed] + 1
                    q.append((nx, ny, crashed))

                # 벽을 부술 수 있는 경우
                if graph[nx][ny] == 1 and crashed == 0:
                    visited[nx][ny][crashed + 1] = visited[x][y][crashed] + 1
                    q.append((nx, ny, crashed + 1))
    return -1


print(bfs(0, 0, 0))
