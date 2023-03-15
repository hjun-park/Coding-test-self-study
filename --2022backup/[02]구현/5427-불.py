import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

T = int(input().rstrip())

# 1) 불의 이동 (불 리스트는 매번 초기화)
# 2) 상근이 이동 ( 불이 옮겨졌거나 불이 붙으려는 칸으로 이동 불가 )

'''
    핵심: https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-5427%EB%B2%88-%EB%B6%88-O-1-Python
        1. visited 좌표에 time을 담거나 불(FIRE)를 담았음
'''


def bfs():
    while q:
        x, y = q.popleft()

        # 현재 좌표에 따라 flag가 달라짐
        if visited[x][y] != "FIRE":
            flag = visited[x][y]  # 좌표가 불이 아닌 경우
        else:  # 좌표가 불이 있는 곳인 경우
            flag = "FIRE"

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1 and (
                    graph[nx][ny] == "." or graph[nx][ny] == "@"
                ):
                    if flag == "FIRE":
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "FIRE":  # 현재 flag가 불이 아니라 사람인데 범위를 벗어나면 탈출한 것임
                    return flag + 1

    return "IMPOSSIBLE"


for _ in range(T):
    M, N = map(int, input().split())
    q = deque()
    visited = [[-1] * M for _ in range(N)]
    graph = []

    for i in range(N):
        graph.append(list(input().rstrip()))
        for j in range(M):
            if graph[i][j] == "@":
                visited[i][j] = 0  # 사람 이동 time 체크
                start = (i, j)
            elif graph[i][j] == "*":
                visited[i][j] = "FIRE"  # 불이 있는 곳은 false, 그 외에는 사람 이동 time 체크
                q.append((i, j))

    q.append(start)
    print(bfs())
