import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    move_cnt = [[0] * M for _ in range(N)]
    move_cnt[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 'x' and not move_cnt[nx][ny]:
                    move_cnt[nx][ny] = move_cnt[x][y] + 1
                    q.append([nx, ny])
    return move_cnt


while True:
    M, N = map(int, input().split())

    if M == 0 and N == 0:
        break

    sx, sy = 0, 0
    graph, dust_list = [], []

    # 1) 시작지와 먼지 리스트 기록
    for i in range(N):
        row = list(input().strip())
        graph.append(row)
        for j, k in enumerate(row):
            if k == 'o':
                sx, sy = i, j
            elif k == '*':
                dust_list.append([i, j])

    # 2) BFS 순환 (청소기로부터 먼지들까지의 거리를 구함)
    vc_to_dust, find_all_dust = [], True
    move_list = bfs(sx, sy)

    # 3) 먼지 리스트 순회하면서 청소가 안 된 구역이 있으면 -1 출력
    for i, j in dust_list:
        if not move_list[i][j]:
            find_all_dust = False
            break
        vc_to_dust.append(move_list[i][j] - 1)  # 이동횟수는 1부터 count 했으므로 -1을 해 줌

    if not find_all_dust:
        print(-1)
        continue

    # 4) 모든 먼지끼리의 거리를 구함 (인접행렬을 만든다)
    dust_to_dust = [[0] * len(dust_list) for _ in range(len(dust_list))]

    for i in range(len(dust_list) - 1):
        move_list = bfs(dust_list[i][0], dust_list[i][1])
        for j in range(i + 1, len(dust_list)):
            dust_to_dust[i][j] = move_list[dust_list[j][0]][dust_list[j][1]] - 1
            dust_to_dust[j][i] = dust_to_dust[i][j]

    # 5) 순열로 갈 수 있는 모든 경로를 구해놓고 거리를 다 더해본 후 최소값 출력
    ans = sys.maxsize
    t = False
    for pm in list(permutations([x for x in range(len(dust_to_dust))])):
        dist = 0
        dist += vc_to_dust[pm[0]]  # 청소기로부터 해당 첫 dust까지의 거리
        dust_start = pm[0]  # 청소기 -> 첫 번째 먼지 이동 후 시작지 지정

        # 나머지 경로를 모두 탐색하면서
        for j in range(1, len(pm)):
            dust_to = pm[j]         # 이동 목적지 지정
            dist += dust_to_dust[dust_start][dust_to]   # 이동까지 거리 추가
            dust_start = dust_to    # 이전 목적지를 시작지로 이동
        ans = min(ans, dist)
    print(ans)
