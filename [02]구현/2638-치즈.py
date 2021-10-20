import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 공기: 두 변이 맞닿은 곳 [ https://it-garden.tistory.com/274 ]
# 1) BFS 순회하여 치즈와 맞닿을 때마다 치즈의 개수를 증가
# 2) 치즈 맞닿은 값이 3이상이라면 녹이고 나머지는 공기 혹은 초기 치즈 상태로 변경


def check_melted_cheese():
    is_melted = False

    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:  # 공기와 맞닿은 부분이 2개 이상인 경우 녹음
                graph[i][j] = 0
                is_melted = True
            elif graph[i][j] == 2:
                graph[i][j] = 1  # 공기와 한 곳만 맞닿은 부분은 초기화

    return is_melted


def bfs():
    q = deque()
    visited = [[False] * M for _ in range(N)]

    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:  # 치즈
                    if graph[nx][ny] >= 1:
                        graph[nx][ny] += 1
                    else:  # 비어있는 공간
                        visited[nx][ny] = True
                        q.append((nx, ny))


answer = 0
while True:
    bfs()

    if check_melted_cheese():
        answer += 1
    else:
        break

print(answer)
