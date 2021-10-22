import sys
from collections import deque

input = sys.stdin.readline

# bfs 관련 함수 수행
# 1) 시작점  x, y를 queue에 tuple 형태로 담기
# 2) 해당 x, y좌표 방문처리
# 3) while queue 시작
# 3-1) queue의 x, y좌표를 꺼냄
# 3-2) 4방향을 돌면서 nx, ny 범위 확인
# 3-3)    방문하지 않았으며 음식물 쓰레기가 있는 경우에
# 3-4)         해당 지점을 방문처리하고 좌표를 queue집어 넣음
# 3-5)          음식쓰레기 좌표를 방문했으니 음식물 크기 += 1
# 3-6) bfs함수가 실행되는 순간은 음식물쓰레기 위치기 때문에 처음에 count=1 부터 시작이다.
def bfs(x, y):
    count = 1   # bfs를 수행하는 위치는 음식물이 있기 때문에 1부터 시작
    # queue = deque((x, y))
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        # queue에서 꺼내고 기존에는 인접 리스트를 확인하면 됐지만
        # 여기서는 갈 수 있는지 없는지부터 판단이 필요함
        # 갈 수 있다면 해당 좌표를 큐에 추가하고 방문처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1  # 음식물쓰레기 개수 증가
    return count





# 1) dx, dy 이동좌표 설정 ( 좌상우하 )
# 2) n, m, k 입력받음 + graph, visited ( 0과 False )
# 3) r, c를 입력받고 음식물 쓰레기 좌표 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1 # 음식물


max_count = 0
# n, m 돌면서 graph해당 위치에 음식물이 있고 방문하지 않았다면
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            max_count = max(max_count, bfs(i, j))
#   bfs를 통해 돈다. 돌고나서 최댓값은 max_count에 비교하여 저장한다.
# 최종적으로 출력
print(max_count)
