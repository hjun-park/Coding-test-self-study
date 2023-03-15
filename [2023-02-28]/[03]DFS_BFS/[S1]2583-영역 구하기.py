import sys
from collections import deque

input = sys.stdin.readline

'''
# =============================================================== #

# [S3]1966-프린터 큐 ( https://www.acmicpc.net/problem/1966 )

# 배운점:
# 0) 두 꼭짓점 좌표가 주어진 상황에서 정사각형을 칠하는 예제 

# =============================================================== #
'''

N, M, K = map(int, input().split())
# (왼쪽아래 x, y // 오른쪽 위 x, y)
point = [list(map(int, input().split())) for _ in range(K)]
visited = [[False] * M for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 사각형 위치 방문처리 (일반적 BFS와 사각형 좌표는 x <-> y 라서 for문 돌 때는 좌표 바꿔서 돌리기 )
def visit_square(square):
    start_x, start_y = square[0], square[1]
    end_x, end_y = square[2], square[3]

    for x in range(start_y, end_y):  # 점 3개는 선분 2개
        for y in range(start_x, end_x):
            try:
                visited[x][y] = True
            except IndexError:
                print(x, y)
                print(start_x, start_y)
                print(end_x, end_y)
                sys.exit(0)


# BFS 돌면서 빈 공간 체크
def bfs(a, b):
    q = deque()
    cnt = 1
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt


# 1) 사각형 위치는 방문처리
for p in point:
    visit_square(p)

# 2) BFS
count = 0
area = []
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            size = bfs(i, j)
            area.append(size)
            count += 1

print(count)
area.sort()
print(' '.join(map(str, area)))
