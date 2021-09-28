import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(N)]  # 벽을 설치한 뒤 리스트

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

'''
    0: 빈칸
    1: 벽
    2: 바이러스
'''
result = 0


def virus_move(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 전파 가능하며 벽이 없는 경우
        #   바이러스 지속 전파
        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_move(nx, ny)


def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1

    return score


def dfs(count):
    global result
    if count == 3:
        # 울타리 백업
        for i in range(N):
            for j in range(M):
                temp[i][j] = graph[i][j]

        # 바이러스가 있는지 체크
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus_move(i, j)

        # 바이러스가 다 퍼지고 난 후에 계산
        result = max(result, get_score())
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                count -= 1  # 백트래킹
                graph[i][j] = 0


dfs(0)
print(result)
