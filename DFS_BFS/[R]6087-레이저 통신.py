import sys
from collections import deque

input = sys.stdin.readline

'''
    참고: https://dirmathfl.tistory.com/301
'''
W, H = map(int, input().split())
visited = [[1e9] * W for _ in range(H)]  # 해당 좌표가 목적지라면 필요한 거울 개수
graph = []
pos = []

# 0, 1, 2, 3 (좌 상 우 하)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for i in range(H):
    graph.append(list(input().rstrip()))
    for j in range(W):
        if graph[i][j] == 'C':
            pos.append((i, j))

start, end = pos

def bfs():
    q = deque([start])
    visited[start[0]][start[1]] = 0 # 시작지 거울 개수 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 벽을 만날 때 까지 같은 방향으로 이동
            while 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != '*':
                # 같은 방향으로 이동하려는 지역의 거울 개수가
                # 기존 위치 + 1 인 거울개수보다 적으면
                # 이미 거울이 설치되있고 최소 거울 개수가 구해진 상태이므로
                # break
                if visited[nx][ny] < visited[x][y] + 1:
                    break

                # q 추가, 거울 최소 개수 설치, nx, ny 이동
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

                # 같은 방향으로 한 칸 이동
                nx += dx[d]
                ny += dy[d]

    return visited[end[0]][end[1]] - 1


print(bfs())
