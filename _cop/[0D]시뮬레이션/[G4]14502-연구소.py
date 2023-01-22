import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
_max = -1  # 안전구역 가장 큰 개수
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

'''
0 : 빈칸
1 : 벽
2 : 바이러스
'''


def spread(temp, x, y):

    # BFS 예시
    q = deque()
    q.append((x, y))
    while q:
        qx, qy = q.popleft()

        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))


    # DFS 예시
    # for d in range(4):
    #     nx = x + dx[d]
    #     ny = y + dy[d]
    #
    #     # 전파 가능하며 벽이 없는 경우
    #     #   바이러스 지속 전파
    #     if 0 <= nx < N and 0 <= ny < M:
    #         if temp[nx][ny] == 0:
    #             temp[nx][ny] = 2
    #             spread(nx, ny)


def get_score(temp):
    global _max

    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1

    _max = max(score, _max)


def dfs(cnt):
    # 1. 벽을 다 세우면
    if cnt == 3:
        # 1. 복사 후
        temp = deepcopy(graph)

        # 2. 처음부터 탐색해서 2라면 바이러스 퍼지기 (BFS)
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 2:
                    spread(temp, i, j)

        # 3. 안전구역 점수 구하기
        get_score(temp)

        return  # TODO : 빼먹으면 안됨

    # 2. 벽을 아직 안 세웠다면
    else:
        # 1. 탐색해서 빈 공간 울타리 설치 후 dfs
        for i in range(N):
            for j in range(M):
                # 1. DFS 탈출하면 다시 복구 (백트래킹)
                if graph[i][j] == 0:
                    cnt += 1
                    graph[i][j] = 1
                    dfs(cnt)
                    cnt -= 1
                    graph[i][j] = 0


dfs(0)
print(_max)
