from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 공기: 두 변이 맞닿은 곳 [ https://it-garden.tistory.com/274 ]
# 1) BFS 순회하여 치즈와 맞닿을 때마다 닿은 공기의 개수를 증가
# 2) 치즈 맞닿은 값이 3이상이라면 녹이고 나머지는 공기 혹은 초기 치즈 상태로 변경


# BFS 순회하여 치즈와 맞닿을 때마다 닿은 공기의 개수를 증가
def bfs():
    q = deque()
    q.append((0, 0))

    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 1개 이상이라면 치즈가 있으므로 해당 좌표에 공기 += 1
            # 0개라면 치즈가 없으므로 방문처리하고 큐에 담아주기
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                elif not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))


# 치즈를 순회하면서 3 이상인 부분은 녹인다. ( 처음값이 1이고 공기 2번 접하면 3이 됨)
def cheese():
    is_melted = False

    for x in range(N):
        for y in range(M):
            if graph[x][y] >= 3:
                graph[x][y] = 0
                is_melted = True
            elif graph[x][y] == 2:  # 2인 부분은 녹일 수 없으므로 다시 1로 초기화
                graph[x][y] = 1

    return is_melted


time = 0
while True:
    bfs()

    # for row in graph:
    #     print(*row)

    if not cheese():  # 치즈가 녹은게 없는 경우 다 녹인 것이므로 탈출
        break

    time += 1

print(time)
