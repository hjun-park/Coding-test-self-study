import sys
from collections import deque

'''
 1) 충분히 여러 번 돌아도 시간초과가 나지 않기 때문에 visited 필요 없음
 2) BFS를 이용한 방식
 3) https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-16197%EB%B2%88-%EB%91%90-%EB%8F%99%EC%A0%84-1-Python
'''
N, M = map(int, input().split())
graph = []
coins = []
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(count, x1, y1, x2, y2):
    queue = deque()
    queue.append((count, x1, y1, x2, y2))

    while queue:
        count, x1, y1, x2, y2 = queue.popleft()

        if count >= 10:
            print(-1)
            return

        for d in range(4):
            nx1 = x1 + dx[d]
            ny1 = y1 + dy[d]
            nx2 = x2 + dx[d]
            ny2 = y2 + dy[d]

            # 1) 벽으로 가는 경우
            if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                if graph[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if graph[nx2][ny2] == '#':  # 여기도 벽이 있을 수 있으니 if로 시작
                    nx2, ny2 = x2, y2

                queue.append((count + 1, nx1, ny1, nx2, ny2))
            # 2) 밖으로 빠지는 경우 (한 동전)
            elif 0 <= nx1 < N and 0 <= ny1 < M:
                print(count + 1)
                return

            # 3) 다른 한 동전 밖으로 빠지는 경우
            elif 0 <= nx2 < N and 0 <= ny2 < M:
                print(count + 1)
                return

            # 4) 두 동전이 밖으로 빠지는 경우
            else:
                continue

    print(-1)
    return


for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] == 'o':
            coins.append((i, j))

bfs(0, coins[0][0], coins[0][1], coins[1][0], coins[1][1])
