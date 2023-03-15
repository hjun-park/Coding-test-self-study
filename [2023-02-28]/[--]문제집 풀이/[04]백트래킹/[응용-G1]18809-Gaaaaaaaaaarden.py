import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M, G, R = map(int, input().split())

# 0: 호수 / 1: 배양액 못 뿌리는 땅 / 2: 배양액 뿌리는 땅
graph = [list(map(int, input().split())) for _ in range(N)]
max_flower = 0

can_start = []
temp = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 3) bfs(green_start, red_start) 함수 순회
def bfs(green_start, red_start):
    # 4) green_q와 red_q를 선언 + flower 와 second = 1 초기화
    green_q = deque([])
    red_q = deque([])
    flower, second = 0, 1

    # 5) green_start, red_start를 순회하면서 visited 배열에 -2로 초기화 + q에 집어넣음
    for s in green_start:
        visited[s[0]][s[1]] = -2
        green_q.append(s)

    for s in red_start:
        visited[s[0]][s[1]] = -2
        red_q.append(s)

    # 6) while green_q and red_q:
    while green_q and red_q:
        # 6-1) 가장 먼저 green_q의 길이만큼 순회함
        for _ in range(len(green_q)):
            x, y = green_q.popleft()

            # 만약 방문한 곳이 꽃(-100)이라면 continue
            if visited[x][y] == -100:
                continue

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # 4방향 순환하면서 graph가 배양 가능한 땅이며(0만 아니면 됨) 방문 한 적이 없다면 (-1)
                if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny] == -1 and graph[nx][ny]:
                        # 방문처리하고 큐 추가, 방문지점엔 second
                        visited[nx][ny] = second
                        # len(green_q)만큼 루프를 도니까 추가된 green_q 값은 이번 second에는 돌지 않음
                        green_q.append((nx, ny))

        # 6-2) red_q 순환
        for _ in range(len(red_q)):
            x, y = red_q.popleft()

            # 만약 방문한 곳이 꽃(-100)이라면 continue
            if visited[x][y] == -100:
                continue

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # 4방향 순환하면서 graph가 배양 가능한 땅이며(0만 아니면 됨) 방문 한 적이 없다면 (-1)
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny]:
                        if visited[nx][ny] == -1:
                            # 방문처리하고 큐 추가 (green에서는 second를 넣어줬지만 red는 단순방문처리)
                            visited[nx][ny] = -2
                            # len(green_q)만큼 루프를 도니까 추가된 green_q 값은 이번 second에는 돌지 않음
                            red_q.append((nx, ny))

                        # 6-1과 다른점은 방문지점이 second라면 -> 같은 second에 녹색배양액이 설치 됨
                        # 서로 만나는 지점이므로 -100 대입 (꽃 만들기)
                        elif visited[nx][ny] == second:
                            flower += 1
                            visited[nx][ny] = -100

        # 6-3) second += 1
        second += 1
    return flower


# 1) 배열을 순회하면서 입력받은 값이 2(배양액을 뿌릴 수 있는 땅)라면 can_start에 넣기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            can_start.append((i, j))

# # [핵심]
# 2) combination 을 이용하여 can_start에서 G+R만큼 뽑은 값으로 순회
for i in combinations(can_start, G + R):
    # 2-1)  2에서 얻어진 배열 i 중에서 G개만큼 green_start로 선정
    for green_start in combinations(i, G):
        # 2-1-1) visited 초기화(-1로)(방문여부와 꽃 체크), red_start 초기화 (배열 i에서 green_start없는 값)
        visited = [[-1] * M for _ in range(N)]
        red_start = [x for x in i if x not in green_start]

        # 2-1-2) BFS 순회하고 return값으로 temp에 저장
        temp = bfs(green_start, red_start)
        # 2-1-3) max_flower 값 갱신
        max_flower = max(max_flower, temp)

print(max_flower)
