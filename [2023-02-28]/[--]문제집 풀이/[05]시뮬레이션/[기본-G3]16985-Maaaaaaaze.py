import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

graph = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

# graph 내의 판을 섞어서 구성한 미로를 집어넣을 배열
maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]

# =========================
# BFS 전용
# =========================
# 위 좌 상 우 하 아래 시계 방향
dx = [0, 0, -1, 0, 1, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [1, 0, 0, 0, 0, -1]

exit_time = []

'''
 문제풀이 핵심
  1) 메인 함수 : permutation을 이용하여 미로 판 쌓는 순서를 정한다.
  2) logic() : 재귀함수 이용하여 입구가 1이 나올 때까지 판을 90도 4번 회전한다.
               나오면 다음 layer를 회전시키고 마지막 판까지 도달하면 출구 확인하여 BFS 순회
'''


def bfs():
    q = deque()
    q.append((0, 0, 0))

    visited = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0

    while q:
        z, x, y = q.popleft()

        if z == 4 and x == 4 and y == 4:  # 출구 도달
            exit_time.append(visited[z][x][y])
            return

        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nz][nx][ny] == -1 and maze[nz][nx][ny] == 1:
                    q.append((nz, nx, ny))
                    visited[nz][nx][ny] = visited[z][x][y] + 1


# 90도 시계방향으로 회전하는 함수
def rotate(layer):
    tmp = [[0] * 5 for _ in range(5)]

    for j in range(5):
        for k in range(5):
            # tmp[5 - 1 - k][j] = maze[layer][j][k]
            tmp[k][4 - j] = maze[layer][j][k]
    maze[layer] = tmp


# 입구 출구 검증
def logic(layer):
    # 마지막 층까지 도달한 경우 출구 확인
    if layer == 5:
        if maze[4][4][4]:  # 출구가 있다면
            bfs()
        return

    for r in range(4):  # 4번까지 회전 가능
        if maze[0][0][0]:  # 입구가 있다면
            logic(layer + 1)  # 다음 층으로 검증
        rotate(layer)


# 순열에 따른 미로 판 쌓기
for p in permutations([0, 1, 2, 3, 4]):
    for i in range(5):
        maze[p[i]] = graph[i]

    # permu 다 채웠으면 logic 순환
    logic(0)

print(min(exit_time) if exit_time else -1)
