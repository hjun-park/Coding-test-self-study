import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

'''
  1) 비의 높이가 H일 때 방문처리
  2) 안전구역의 개수를 세는 방법
  
  반례 찾기가 어려웠음, 아무 지역도 물에 잠기지 않는다면 ?
   -> for문을 0부터 시작하면 됐었다. (물에 잠기지 않는 경우도 있다했으니까)
     +) graph에서 최댓값 찾는 방법 
       H = max(map(max, graph))
'''

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


Max = max(map(max, graph))
answer = -1

for h in range(Max):
    temp = 0
    visited = [[False] * N for _ in range(N)]
    # 높이가 h 이하인 부분은 방문 처리
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= h :
                visited[i][j] = True

    # 안전구역의 개수룰 셈
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
                temp += 1

    answer = max(answer, temp)

print(answer)
