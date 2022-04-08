import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[deque() for _ in range(N)] for _ in range(N)]  # 스위치 저장하는 그래프
visited = [[False] * N for _ in range(N)]  # 방문 여부 확인
light = [[False] * N for _ in range(N)]  # 불이 켜져 있는지 여부 확인
light[0][0] = True

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

cnt = 1


def bfs(start_x, start_y):
    global cnt
    q = deque()
    q.append((start_x, start_y))

    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        # 스위치 켜는 시간
        for switch_x, switch_y in graph[x][y]:
            if not light[switch_x][switch_y]:
                light[switch_x][switch_y] = True
                cnt += 1

                # =======================================================
                # 핵심: 불을 켜 준 곳이 방문 가능하면 q에 넣어줘야 가서 불을 켤 수 있다.
                # =======================================================
                # 만약 불 켠 곳의 상하좌우에 방문 기록이 있다면 q에 넣어준다.
                for d in range(4):
                    nx = switch_x + dx[d]
                    ny = switch_y + dy[d]

                    if 0 <= nx < N and 0 <= ny < N:
                        if visited[nx][ny]:
                            q.append((nx, ny))

        # 주변 순회 하면서 미방문 and 불 켜진 곳 탐색
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and light[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


for _ in range(M):
    i, j, a, b = map(int, input().split())
    graph[i - 1][j - 1].append((a - 1, b - 1))

bfs(0, 0)
print(cnt)
