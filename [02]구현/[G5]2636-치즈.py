import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 핵심 0에서부터 시작하고 1하고 만나는 부분은 방문처리하고 0으로 녹인다.
def check_outside():
    q = deque()
    q.append((0, 0))
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    count = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                # 0인 부분은 방문처리하고 queue에 집어넣는다.
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

                # 1인 부분은 방문처리하고 0으로 녹인 후에 count를 증가시킨다.
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = True
                    count += 1

    cheese.append(count)
    return count


cheese = []
time = 0
while True:
    cnt = check_outside()

    # 치즈가 다 녹아서 더이상 녹일게 없었다면 시간추가없이 break
    if cnt == 0:
        break

    time += 1

print(time)
print(cheese[-2])  # -1 맨 끝부분은 다 녹여서 없어진 치즈
#
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# '''
#     핵심 https://hooongs.tistory.com/264
#     1. 처음은 무조건 비어 있으므로 0, 0 부터 BFS를 돌리면 안쪽 0에는 접근하지 않을 수 있다.
#     2. 0을 만나면 큐에 집어넣고 1을 만나면 치즈갯수를 증가시키고 0으로 바꾸어 준다.
#     3. 무한루프로 BFS에 들어가면서 BFS에 들어간 횟수를 time으로 count 한다.
#
#     위 방식대로 여러 번 진행하면 정답을 얻을 수 있음
#
#
#     순서
#     1) 입력, 이동방향 정의, 치즈 배열, 시간 초기화
#     2) 무한루프 시작, 시간 증가, 공기를 찾는 BFS 시작
#     2-1) 0[공기]인 경우 방문처리 후 큐에 집어넣는다.
#     2-2) 1[치즈]인 경우 방문처리 후 count 증가 및 0으로 초기화 한다.
# '''
#
# N, M = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
#
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
#
#
# def count_cheese():
#     visited = [[False] * M for _ in range(N)]
#     q = deque()
#     q.append((0, 0))
#     count = 0
#
#     while q:
#         x, y = q.popleft()
#
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#
#             if 0 <= nx < N and 0 <= ny < M:
#                 if not visited[nx][ny] and graph[nx][ny] == 0:
#                     visited[nx][ny] = True
#                     q.append((nx, ny))
#
#                 if not visited[nx][ny] and graph[nx][ny] == 1:
#                     count += 1
#                     visited[nx][ny] = True
#                     graph[nx][ny] = 0
#
#     cheese.append(count)
#     return count
#
#
# time = 0
# cheese = []
# while True:
#     cnt = count_cheese()
#
#     # 치즈가 다 녹았으면
#     if cnt == 0:
#         break
#
#     time += 1
#
# print(time)  # 다 녹은 시점
# print(cheese[-2])
