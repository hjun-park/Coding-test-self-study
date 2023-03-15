import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 방향 정의 [상, 하, 좌, 우]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):  # 행열이동
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 거라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 괴물이 있는 부분이라면 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 방문하지 않았다면 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 해당 노드에 최단거리 + 1 (기존 기록 거리)
                queue.append((nx, ny))

        # 가장 오른쪽 아래 ( 도착지 ) 반환
        return graph[n - 1][m - 1]


print(bfs(0, 0))
