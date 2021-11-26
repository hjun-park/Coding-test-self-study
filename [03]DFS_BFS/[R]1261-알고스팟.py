import sys
from collections import deque

input = sys.stdin.readline

'''
    1) 가중치를 이용하는 점 ( 벽 부순 횟수를 기록함 )
    2) BFS는 DFS와 다르게 for문 순환할 필요가 없다.
'''

M, N = map(int, input().split())
graph = []


# 벽을 부순 횟수를 기록할 가중치 리스트
dist = [[-1] * M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    dist[0][0] = 0

    while queue:
        qx, qy = queue.popleft()

        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if dist[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        dist[nx][ny] = dist[qx][qy]
                        queue.appendleft((nx, ny))

                    else:
                        dist[nx][ny] = dist[qx][qy] + 1
                        queue.append((nx, ny))


BFS(0, 0)
print(dist[N - 1][M - 1])
