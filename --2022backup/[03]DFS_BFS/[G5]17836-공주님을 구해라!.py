import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

visited = [[False] * M for _ in range(N)]
gram = int(1e9)


def bfs():
    global gram
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True

    while q:
        x, y, t = q.popleft()

        # 검이 있는 경우 공주까지 한 번에 거리 계산
        if graph[x][y] == 2:
            gram = (N - 1 - x) + (M - 1 - y) + t

        # 공주를 찾은 경우 검 거리와 최소 길이 결정 후 반환
        if x == N - 1 and y == M - 1:
            return min(t, gram)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, t + 1))

    # 리턴값은 큰 갑으로 설정 :: 여기서는 위에 그람 시간을 1e9로 할당해놓아서 그거로 결정함
    return gram


res_time = bfs()
print("Fail" if (res_time > T) else res_time)
