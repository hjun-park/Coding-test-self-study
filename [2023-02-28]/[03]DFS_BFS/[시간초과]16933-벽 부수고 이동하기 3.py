import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]  # 거리 기록

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs_v2(start_x, start_y, crashed):
    q = deque()
    q.append((start_x, start_y, crashed))
    visited[start_x][start_y][crashed] = 1
    day = True

    while q:
        for _ in range(len(q)):  # 낮과 밤을 q 길이 만큼 처리함
            x, y, crashed = q.popleft()

            if x == N - 1 and y == M - 1:
                return visited[x][y][crashed]

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                # 벽을 부수지 않는 경우
                if graph[nx][ny] == 0 and visited[nx][ny][crashed] == 0:
                    q.append((nx, ny, crashed))
                    visited[nx][ny][crashed] = visited[x][y][crashed] + 1

                # 벽을 부수는데 낮인 경우 벽을 부수고 이동
                if graph[nx][ny] == 1 and crashed < K:
                    if day:
                        q.append((nx, ny, crashed + 1))
                        visited[nx][ny][crashed + 1] = visited[x][y][crashed] + 1
                    # 벽을 부수는데 밤인 경우 기존 자리 이동횟수만 증가
                    else:
                        q.append((x, y, crashed))
                        # visited[x][y][crashed] += 1

        day = not day
    return -1


print(bfs_v2(0, 0, 0))
