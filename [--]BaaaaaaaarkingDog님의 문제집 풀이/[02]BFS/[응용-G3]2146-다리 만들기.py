import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def find_bfs(start_x, start_y, index):
    global visited

    q = deque()
    visited[start_x][start_y] = True
    graph[start_x][start_y] = index
    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = index


def shortest_bfs2(num):
    # 2-1) 거리를 기록할 visited와 min_dist 선언
    visited = [[-1] * N for _ in range(N)]
    q = deque()

    # 2-2) graph 전체를 순회하면서 num인 부분은 queue에 집어넣어주고 거리 0으로 초기화
    # -> 특정 num을 가진 섬은 전체 한번씩 확인할 예정, 따라서 거리 0으로 초기화
    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                visited[i][j] = 0
                q.append((i, j))

    # 2-3) 큐를 돌며 BFS 시작
    #   - 0이 아니고 다른 섬 번호를 만나면 해당 visited 값에 거리를 새로 갱신하고 최솟값은 min_dist에 할당
    #   - 만약 0이고(바다) 거리도 -1이라면(미방문 상태) q에 넣어주고 visited +1 처리
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                # 2-4) graph[nx][ny] != num이라면 가장 먼저 다른 섬을 먼저 만난 것이므로 거리 return
                if graph[nx][ny] != num and graph[nx][ny] != 0:
                    return visited[x][y]

                # 2-5) 방문하지 않았으면서 바다인 경우에만 q에 집어넣고 거리 방문처리
                if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


# 1) 섬에 index 번호 주기
visited = [[False] * N for _ in range(N)]
index = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and not visited[i][j]:
            index += 1
            find_bfs(i, j, index)

# 2) 섬과 섬끼리 가장 가까운 거리 구하기
cnt = index  # 섬의 개수
answer = int(1e9)
for i in range(1, cnt + 1):
    answer = min(answer, shortest_bfs2(i))

print(answer)
