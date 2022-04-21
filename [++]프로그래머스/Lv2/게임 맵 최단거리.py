from collections import deque

N, M = 0, 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(maps, start_x, start_y):
    q = deque()
    q.append((start_x, start_y))

    visited = [[-1] * M for _ in range(N)]
    visited[start_x][start_y] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx == N - 1 and ny == M - 1:
                return visited[x][y] + 1

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1 and maps[nx][ny] != 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return -1


def solution(maps):
    global N, M
    N = len(maps)
    M = len(maps[0])
    return bfs(maps, 0, 0)


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
