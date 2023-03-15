import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

'''
 1) 벽 3개 ( 3개 미만이면 바이러스 시작 X )
 2) 0(빈칸) 1(벽) 2(바이러스)
'''


def get_score(copied_graph):
    count = 0
    for i in range(N):
        for j in range(M):
            if copied_graph[i][j] == 0:
                count += 1

    return count


def spread_virus(copied_graph, x, y):
    q = deque()
    q.append((x, y))
    while q:
        qx, qy = q.popleft()

        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]

            if 0 <= nx < N and 0 <= ny < M and copied_graph[nx][ny] != 1 and copied_graph[nx][ny] != 2:
                if copied_graph[nx][ny] == 0:
                    copied_graph[nx][ny] = 2
                    q.append((nx, ny))

    # for row in copied_graph:
    #     print(*row)
    # print()
    return copied_graph


max_score = -1  # 안전영역 최대 크기


def dfs(cnt):
    global max_score
    if cnt == 3:
        copied_graph = deepcopy(graph)

        for i in range(N):
            for j in range(M):
                if copied_graph[i][j] == 2:
                    copied_graph = spread_virus(copied_graph, i, j)
        # q에서 바이러스를 빼면 안됨
        max_score = max(max_score, get_score(copied_graph))

        return  # 백트래킹 끝부분은 꼭 return 사용

    else:  # 울타리 세우기
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    cnt += 1
                    dfs(cnt)
                    cnt -= 1
                    graph[i][j] = 0  # 복구


dfs(0)
print(max_score)
