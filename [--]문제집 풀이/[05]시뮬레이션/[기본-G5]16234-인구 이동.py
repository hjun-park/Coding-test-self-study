import sys
from collections import deque

input = sys.stdin.readline

'''
    [요약]
    0. 인접한 나라 사이에는 국경선이 존재
    1. 인구이동은 하루동안 아래 방식으로 진행하며 더 이상 인구이동 없을 때까지 지속
    
    [풀이]
    1. 입력
    2. break 할 때까지 순환 (is_move, 입력 초기화)
     2-1. 방문하지 않았다면 BFS 순환
     2-2. BFS는 union을 관리하는 q와 BFS 전용 q로 구성
     2-3. 범위 내에 있다면 차를 비교해보고 차도 만족하는 경우
      2-3-1. 큐 추가, 유니온 추가, 사람 추가, 연합국 개수 추가
     2-4. BFS 방문 처리 후 연합 인원을 구함
     2-5. 연합국 개수가 2개 이상이라면 is_move 처리 후 union에 대해서 사람 반영
    3. 모든 BFS 방문 마친 후에는 is_move 따라서 day를 추가할 지 break 할 건지 생각
     
    [주의점]
    1. 너무 visited로만 처리하려고 해서 문제가 복잡해졌었다.

'''

N, L, R = map(int, input().split())  # L, R = 인구 이상 이하
graph = [list(map(int, input().split())) for _ in range(N)]
day = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(visited, a, b, graph):
    global is_moved

    # 2-2) BFS는 union을 관리하는 queue와 BFS를 관리하는 queue로 구성
    q = deque()
    union_q = deque()

    q.append((a, b))
    union_q.append((a, b))

    visited[a][b] = True
    cnt = 1  # 연합국 개수
    people = graph[a][b]  # 연합 사람 수

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 2-3) 범위 내에 있다면 차이를 비교해보고 이것도 만족하는 지 확인
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    # 2-3-1) 만족하는 경우 다음 항목 추가 ( 큐, 유니온, 사람, 연합국 개수, 방문처리 )
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union_q.append((nx, ny))
                    cnt += 1  # 연합국 개수 추가
                    people += graph[nx][ny]  # 연합국 사람 추가

    # 2-4) BFS 방문처리 후 연합 인원 구성
    union_people = people // cnt

    # 2-5) 연합국 개수가 2개 이상이라면 인원을 분배
    if cnt >= 2:
        is_moved = True

        for r, c in union_q:
            graph[r][c] = union_people


# 2) break 할 때까지 순환
while True:
    is_moved = False
    visited = [[False] * N for _ in range(N)]

    # 2-1) 방문하지 않았다면 BFS 순환
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(visited, i, j, graph)

    # 3. 방문 종료 후 is_moved 따라서 day를 추가할 지 아니면 루프를 벗어날 지 결정
    if is_moved:
        day += 1
    else:
        break

print(day)
