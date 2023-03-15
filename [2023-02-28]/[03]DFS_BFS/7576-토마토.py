import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

q = deque()

# 1) 큐에 익은 토마토의 좌표위치를 저장
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))


# 2) BFS를 순회하며 토마토를 익혀감,
# 익어가는 새로운 토마토는 이전 토미토 +1 더해질 것이다.
def bfs():
    # 0, -1, 1로 구분될 것이므로 방문리스트는 필요 없음
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:  # 안 익은 토마토가 있따면
                    graph[nx][ny] = graph[x][y] + 1  # 이전 익은 토마토에서 +1
                    q.append((nx, ny))


bfs()
day = 0
# 3) BFS를 돌았음에도 불구하고 graph[i][j] == 0 인 익지 않은 토마토가 있다면 -1 출력 종료
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:  # 안 익은 토마토가 있다.
            print(-1)
            sys.exit(0)

    day = max(day, max(graph[i]))

print(day - 1)
