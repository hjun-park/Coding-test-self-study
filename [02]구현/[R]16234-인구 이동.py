import sys
from collections import deque

input = sys.stdin.readline

'''
    [흐름]
    1) 입력 (dx, dy, graph, is_move(국경이동 유무), visited)
    2) 모든 좌표를 하나씩 순환하는데, 방문하지 않은 경우 DFS 순환
    [DFS]
    2-1) 큐에 기존 좌표 추가 
    2-2) 큐 꺼냄, 범위 체크, 방문 체크
    2-3) 국가 인원 수 범위 체크
    2-3-1) 범위 안에 있다면 방문처리 및 큐 추가 및 연합국 count 추가, temp에 추가,
    2-4) 모든 연합 속한 나라의 인원들을 맞춰줌
'''
N, L, R = map(int, input().split())
graph = []
day_count = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y, visited, graph):
    global is_moved  # 인구 이동 여부
    people = graph[x][y]  # 연합국 총 인원 수
    count = 1  # 연합국의 수

    queue = deque()  # BFS 전용 큐
    queue.append((x, y))  # BFS 전용 큐 추가
    visited[x][y] = True

    union = list()
    union.append((x, y))

    while queue:
        px, py = queue.popleft()

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if visited[nx][ny] is True:
                continue

            if L <= abs(graph[px][py] - graph[nx][ny]) <= R:
                visited[nx][ny] = True
                count += 1  # 연합국 추가
                queue.append((nx, ny))
                people += graph[nx][ny]
                union.append((nx, ny))

    # 큐의 모든 조회 ( BFS를 다 돈 후에는 모든 연합 인원 분배 )
    people_count = people // count
    # 인구 이동
    if count > 1:
        is_moved = True
        for x, y in union:
            graph[x][y] = people_count


for _ in range(N):
    graph.append(list(map(int, input().split())))

# while 한 번 = 하루 인구 이동
while True:
    is_moved = False
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, visited, graph)

    # visited 체크
    if is_moved:
        day_count += 1
    else:
        break

print(day_count)
