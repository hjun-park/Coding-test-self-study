import sys
from collections import deque

input = sys.stdin.readline

N, M = 12, 6
graph = [list(input().rstrip()) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

'''
    5. 만약 터뜨린게 없으면 while문 탈출 있으면 블록을 내리는 작업
    6. [블록내리기] 3중 for문을 이용할 것 ( 열 단위 -> 행 단위 -> -1부터 행까지 단위 )
        1) phase
         (10, 0) <-> (11, 0)
        2) phase
         (9, 0) <-> (11, 0)
         (9, 0) <-> (10, 0)
'''


# 해당 자리를 제거하고 중력에 의해 블록이 내려가는 모습
# 만약 터뜨리면 그 자리는 .으로 표시한다.
# y가 '.'이 아니면서 그 아래부분을 나타내는 z가 '.' 이라면 중력적용이 안 된 경우이다. 그래서 아래로 내려준다.
# z가 돌면서 숫자들이 맨 아래로 오도록 하나씩 내려준다.
def down():
    for x in range(M):  # 각 열마다 확인
        for y in range(N - 1, -1, -1):  # 행의 맨 아래서부터 확인
            for z in range(N - 1, y, -1):  # 마찬가지로 y이후 행의 맨 아래서부터 확인
                if graph[y][x] != '.' and graph[z][x] == '.':
                    graph[z][x] = graph[y][x]
                    graph[y][x] = '.'
                    break


def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))

    visited[start_x][start_y] = True
    trace = [(start_x, start_y)]
    color = graph[start_x][start_y]

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 내 and 미방문 and 뿌요 색깔 같은 경우
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    trace.append((nx, ny))

    # 순환 이후 4개 이상인 경우 뿌요 터뜨림
    if len(trace) >= 4:
        # print(trace)
        for tx, ty in trace:
            graph[tx][ty] = '.'

        return 1

    return 0


visited = [[False] * M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        # 뿌요가 있는 경우 and 미방문 상태
        if graph[i][j] != '.' and not visited[i][j]:
            # print(f'시작 : {graph[i][j]}')
            cnt += bfs(i, j)

            # 한 번 연쇄적으로 터뜨린 이후 중력에 의해 아래로 떨어뜨린다.
            down()

            # 블록들의 위치가 재배치되었으므로 방문처리 초기화
            visited = [[False] * M for _ in range(N)]

            # print()
            # for row in graph:
            #     print(*row)
            # print(f'카운트 증가: {cnt}')

            # =================================================
            # 문제점
            #   - 문제에서는 "한 번 클릭으로" 연쇄적으로 뿌요가 몇 번 터지는 지를 물어봄
            #   - 지금 푼 방식은 "총 몇 번 클릭"해야 터지는 지로 풀었음
            # =================================================

print(cnt)
