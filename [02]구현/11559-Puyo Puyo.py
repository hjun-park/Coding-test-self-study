import sys
from collections import deque

input = sys.stdin.readline

graph = [list(input().rstrip()) for _ in range(12)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, M = 12, 6

# 1. 같은 색이 depth 4 이상인 경우
# 2. 해당 자리를 제거하고 중력에 의해 블록이 내려가는 모습

''' https://pacific-ocean.tistory.com/390
    1. 방문그래프 생성 + 터뜨림 여부 확인하는 Flag 생성 ( while 무한루프 시작 )
    2. 그래프 탐색, ( .이 아니면서 방문한 적이 없는 경우 방문처리 후 BFS 탐색 
    3. BFS 탐색 시 특별한 점은 deque그리고 chain이라는 터뜨릴 좌표를 담는 리스트도 함께 이용한다.
    4. BFS 탐색이 끝나고 chain 길이가 4가 넘으면 flag=True 설정, chain을 돌면서 관련좌표는 '.'으로 변경
    5. 만약 터뜨린게 없으면 while문 탈출 있으면 블록을 내리는 작업
    6. [블록내리기] 3중 for문을 이용할 것
        1) phase
         (10, 0) <-> (11, 0)
        2) phase
         (9, 0) <-> (11, 0)
         (9, 0) <-> (10, 0)
'''


# 이해하기 힘든 부분
# 뿌요뿌요 판을 예시로 실제 좌표 찍어가면서 알아보는 수밖에 없음
def down():
    for x in range(M):
        for y in range(N-1, -1, -1):
            for z in range(N-1, y, -1):
                if graph[y][x] != '.' and graph[z][x] == '.':
                    graph[z][x] = graph[y][x]
                    graph[y][x] = '.'
                    break


def bfs(a, b, ch):
    q = deque()
    chain = []

    q.append((a, b))
    chain.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == ch:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    chain.append((nx, ny))

    return chain


answer = 0
while True:
    flag = False
    visited = [[False] * M for _ in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(M):
            if graph[i][j] != '.' and not visited[i][j]:
                array = bfs(i, j, graph[i][j])

                if len(array) >= 4:
                    flag = True
                    for x, y in array:
                        graph[x][y] = '.'

    if not flag:
        break

    down()
    answer += 1

print(answer)
