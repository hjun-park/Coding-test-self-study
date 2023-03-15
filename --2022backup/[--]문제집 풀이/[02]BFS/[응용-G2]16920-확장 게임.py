import sys
from collections import deque

input = sys.stdin.readline

N, M, P = map(int, input().split())  # 플레이어 수 P
S = [0] + list(map(int, input().split()))
graph = [list(input().rstrip()) for _ in range(N)]

# 플레이어 별 가지고 있는 성 리스트
castle = [[] for _ in range(P + 1)]
tmp_castle = [[] for _ in range(P + 1)]
cnt = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 1) 맵을 돌면서 '.', '#', '번호'에 따라 다르게 처리
for i in range(N):
    for j in range(M):
        if graph[i][j] == '.':
            cnt += 1
        elif graph[i][j] == '#':
            continue
        else:  # 숫자라면 각 플레이어 배열에 성의 위치를 대입
            castle[int(graph[i][j])].append((i, j))
            tmp_castle[int(graph[i][j])].append((i, j))
            cnt += 1


# 이번 턴에 확장된 영역이 없는지 체크하는 함수
def fin():
    rans = 0
    for i in range(1, P + 1):
        rans += len(tmp_castle[i])

    if rans == 0:
        return True
    return False


def bfs(player_num):
    q = deque()
    visited = [[-1] * M for _ in range(N)]

    # 해당 플레이어가 가지고 있는 모든 성들을 q에 대입 후 0으로 셋팅
    while tmp_castle[player_num]:
        start_x, start_y = tmp_castle[player_num].pop(0)
        q.append((start_x, start_y))
        visited[start_x][start_y] = 0

    while q:
        x, y, = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                # 미방문 and '.'이라면
                # 방문처리 거리 카운트 + tmp_castle 등록 + graph 변경
                if visited[nx][ny] == -1 and graph[nx][ny] == '.':
                    visited[nx][ny] = visited[x][y] + 1
                    tmp_castle[player_num].append((nx, ny))
                    graph[nx][ny] = str(player_num)

                    # visited에는 이동한 횟수가 기록되는데, 그게 S[플레이어번호] 보다 작다면 q에 집어넣기
                    if visited[nx][ny] < S[player_num]:
                        q.append((nx, ny))

    # visited = [[-1] * M for _ in range(N)]


turn = 1
while True:
    if fin():
        break

    # 한 턴 다 돌았으면 다시 시작
    if turn == P + 1:
        turn = 0
    bfs(turn)

    for i in range(len(tmp_castle[turn])):
        castle[turn].append(tmp_castle[turn][i])

    turn += 1

for i in range(1, P + 1):
    print(len(castle[i]), end=' ')

# ============================================
# 시간초과 소스
# ============================================
# while True:
#     is_expand = False
#     for p in range(1, P + 1):
#         copied_graph = deepcopy(graph)
#         for x in range(N):
#             for y in range(M):
#                 if graph[x][y] != '.' and graph[x][y] != '#':
#                     if int(graph[x][y]) == p:
#                         for d in range(4):
#                             nx = x
#                             ny = y
#                             for _ in range(S[p]):
#                                 nx += dx[d]
#                                 ny += dy[d]
#
#                                 if 0 <= nx < N and 0 <= ny < M:
#                                     if graph[nx][ny] == '.':
#                                         copied_graph[nx][ny] = p
#                                         is_expand = True
#
#         graph = deepcopy(copied_graph)
#
#     if not is_expand:
#         break
#
# result = defaultdict(int)
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] != '.' and graph[i][j] != '#':
#             result[int(graph[i][j])] += 1
#
# result = dict(sorted(result.items()))
# print(*result.values())
