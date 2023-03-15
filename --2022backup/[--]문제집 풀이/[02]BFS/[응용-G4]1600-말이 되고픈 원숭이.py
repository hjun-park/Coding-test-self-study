import sys
from collections import deque

input = sys.stdin.readline

moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 원숭이는 K번만 말처럼 이동 가능, 그 이후는 인접한 칸으로만 이동 가능

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0 for _ in range(31)] for _ in range(W)] for _ in range(H)]

    while q:
        x, y, cnt = q.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][cnt]

        '''
         내가 한 실수:
          - 이렇게 하면 대각선 먼저, 이후 상하좌우가 돌게 된다. (visited를 대각선 먼저 체크하니까)
          - [1] 대각선과 상하좌우 도는걸 분리하자.
          
          - [1] 그럼 어떻게 분리할건데? => 차원을 늘려준다. 기존 2차원에서 3차원으로.
          - visited를 3차원 배열로 만들었다. x는 Height, y는 Width, cnt는 z축으로 원숭이가 말처럼 몇 번 이동했는지 체크
          - 이렇게 해서 원숭이가 인접향 4방향을 먼저 돌고 그 다음에는 말처럼 이동했다는 의미로 cnt + 1 해서 대각선(말 이동방향) 이동한다.
          [참고](https://pacific-ocean.tistory.com/393)
        '''

        # 1) 4방향 이동 먼저
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < H and 0 <= ny < W:
                if visited[nx][ny][cnt] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cnt))

        # 2) 대각선(말의 방향) 대로 이동 가능한 경우
        if cnt < K:
            for m in moves:
                nx = x + m[0]
                ny = y + m[1]

                if 0 <= nx < H and 0 <= ny < W:
                    if visited[nx][ny][cnt + 1] == 0 and graph[nx][ny] == 0:
                        visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                        q.append((nx, ny, cnt + 1))

    return -1


K = int(input().rstrip())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

print(bfs())
