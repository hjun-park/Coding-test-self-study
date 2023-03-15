import sys
from collections import deque

input = sys.stdin.readline

'''
    참고: https://wookcode.tistory.com/167
'''

R, C = map(int, input().split())
Dx, Dy = 0, 0

graph = [list(input().rstrip()) for _ in range(R)]
dist = [[0] * C for _ in range(R)]  # 해당 좌표까지의 최소거리
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

q = deque()


def bfs(Dx, Dy):
    while q:
        x, y = q.popleft()

        if x == Dx and y == Dy:
            return dist[x][y]

        # if graph[Dx][Dy] == 'S':
        #     return dist[Dx][Dy]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 체크
            if 0 <= nx < R and 0 <= ny < C:
                # 이동대상이 S(고슴도치)이며 이동하려는 위치에 . 이거나 D(집)인 경우
                # 고슴도치 이동 + 이동거리 저장 + 큐 추가
                if graph[x][y] == 'S' and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                    graph[nx][ny] = 'S'
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

                # 이동대상이 *(물)이며 이동하려는 위치에 . 이거나 S(고슴도치)인 경우
                # 물 이동 (고슴도치가 있다면 그것도 물로 덮어버림) + 큐 추가
                if graph[x][y] == '*' and (graph[nx][ny] == '.' or graph[nx][ny] == 'S'):
                    graph[nx][ny] = '*'
                    q.append((nx, ny))
    return "KAKTUS"


# 고슴도치와 비버집 좌표를 찾음
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            q.append((i, j))  # 고슴도치
        elif graph[i][j] == 'D':
            Dx, Dy = i, j  # 비버집은 목적지기 때문에 좌표를 따로 저장

# 물의 좌표를 큐에 나중에 집어넣은 이유는
#  고슴도치가 먼저 이동하고 그 다음에 물이 차게 하기 위함
for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            q.append((i, j))

print(bfs(Dx, Dy))
