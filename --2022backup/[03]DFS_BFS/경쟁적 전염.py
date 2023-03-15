import sys
from collections import deque

# 정사각행렬 n  // 바이러스 개수 k개
n, k = map(int, input().split())
graph = []  # 전체 보드 정보 담음
data = []  # 바이러스에 대한 정보를 담음

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):  # 입력된 정보를 확인
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            data.append(graph[i][j], 0, i, j)  # 바이러스 종류, 시간, x, y 좌표

# 정렬 이후에 큐로 옮김
data.sort()
q = deque(data)

# s초 뒤에 x, y에 있는 바이러스는?
target_s, target_x, target_y = map(int, input().split())

# 바이러스가 빠져나갈 수 있는 길
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

    # BFS
while q:
    virus, s, x, y = q.popleft()

    # 정확히 s초가 지나가거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 4 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #  해당 위치로 이동할 수 있는 경우
        if 0 <= nx < n and 0 <= ny and ny < n:
            # 이동한 위치가 아직 방문하지 않았다면, 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append(virus, s + 1, nx, ny)

print(graph[target_x - 1][target_y - 1])

