import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def bfs():
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                # 미 방문 상태이며 벽이 아닌 방문 가능한 경우
                if visited[nx][ny] == 0 and graph[nx][ny] != 1:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    count[nx][ny] = count[x][y] + 1


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
graph = []
can_virus = []

total_block = 0
INF = int(1e9)
result = INF

# 1) 입력 받으면서 바이러스는 따로 추가(2) 벽이 아닌 부분은 b 추가
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(N):
        if line[j] == 2:
            can_virus.append([i, j])
        if line[j] != 1:
            total_block += 1

# 2) Combination 을 이용해 바이러스 활성화 선택지를 만든다.
for i in list(combinations(can_virus, M)):  #
    count = [[-1] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque()

    # 3) 바이러스 있는 지역은 방문 / 카운트 배열은 0초로 초기화 후 q에 집어넣음
    for x, y in i:
        visited[x][y] = 1
        count[x][y] = 0
        q.append([x, y])

    # 4) BFS 순회
    bfs()

    # 5) 방문한 블록을 센다.
    cnt = 0
    for j in visited:
        cnt += j.count(1)

    # 6) 핵심
    # 방문해야 하는 블록의 총 개수와 방문한 cnt 개수가 같다면 실행
    # 벽이 아니면서 바이러스 시작점이 아닌 부분은 count에 반영 (시작점은 0초니까 돌 필요 없음)
    # 그렇게 해서 첫 번째 바이러스 활성화 선택지에 대한 초를 구하게 된다.
    if total_block == cnt:
        max_n = 0
        for j in range(N):
            for k in range(N):
                if graph[j][k] != 1 and [j, k] not in can_virus:
                    max_n = max(max_n, count[j][k])
        result = min(result, max_n)
print(result if result != INF else -1)
