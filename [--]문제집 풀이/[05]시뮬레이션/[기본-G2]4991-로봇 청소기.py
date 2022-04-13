import sys
from collections import deque

input = sys.stdin.readline

'''
    [요약]
    1. 로봇 청소기 사이즈 1x1
    2. 로봇 청소기는 가구가 놓여진 칸에 이동 불가
    3. 같은 곳을 여러 번 방문 가능
    
    4. 더러운 칸의 개수는 10개 넘지 않음
    
    [구할 것]
    1. 더러운 칸을 깨끗한 칸으로 만드는 데 필요한 이동 횟수의 최솟값
    
'''

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(a, b):
    global visited
    q = deque()
    q.append((a, b, 0, 0))

    visited[a][b] = True

    while q:
        x, y, move, eat_dust = q.popleft()

        if eat_dust == dust:
            return move

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if graph[nx][ny] == '.':  # 빈 공간
                        visited[nx][ny] = True
                        q.append((nx, ny, move + 1, eat_dust))

                    elif graph[nx][ny] == '*':  # 먼지
                        print(f'먼지 방문 : {nx, ny}')
                        visited = [[False] * M for _ in range(N)]
                        q = deque()
                        q.append((nx, ny, move + 1, eat_dust + 1))
                        graph[nx][ny] = '.'
                        break  # 먼지 추가 되면 4방향 탐색 끊기

    return -1


while True:
    M, N = map(int, input().split())
    graph = []
    start_x, start_y = 0, 0
    visited = [[False] * M for _ in range(N)]
    dust = 0

    if M == 0 or N == 0:
        break

    for i in range(N):
        line = list(input().rstrip())
        graph.append(line)

        for j in range(M):
            if line[j] == 'o':
                start_x, start_y = i, j
                graph[i][j] = '.'
            elif line[j] == '*':
                dust += 1

    print(bfs(start_x, start_y))
