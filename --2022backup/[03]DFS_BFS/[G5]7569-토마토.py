import sys
from collections import deque

input = sys.stdin.readline

# 가로 / 세로 / 높이
M, N, H = map(int, input().split())
graph = []
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
q = deque()

# 위 / 좌 상 우 하 / 아래
dx = [0, 0, -1, 0, 1, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [-1, 0, 0, 0, 0, 1]

flag = False

def bfs():
    while q:
        x, y, z = q.popleft()
        visited[z][x][y] = True

        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    q.append((nx, ny, nz))
                    graph[nz][nx][ny] = graph[z][x][y] + 1  # 토마토 값을 day로 처리
                    visited[nz][nx][ny] = True


# 1) 입력
for _ in range(H):
    graph.append([list(map(int, input().split())) for _ in range(N)])

# 2) 토마토 좌표는 따로 queue에 저장
for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 1:
                q.append((x, y, z))

# 3) 일단 받은 토마토 좌표에 대해 BFS 순환
bfs()

max_num = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 0:
                flag = True
            max_num = max(max_num, graph[z][x][y])
if flag:
    print(-1)
else:
    print(max_num - 1)
