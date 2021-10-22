import sys
sys.setrecursionlimit(10000)    # 재귀 한도를 풀어줌

'''
    main 함수
    1) 가로세로 0인 Matrix 생성
    2) 좌표보면서 1 찍기
    3) 이중 for문 돌리면서 좌표 1 찾기
    4) 1을 찾는 순간 바로 DFS 순회
    
    dfs 함수 
    1) 방문처리 
    2) 좌표 탐색, 탐색 가능 좌표 있으면 재귀

'''

# 좌, 우, 상, 하
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    # 1. 방문처리 & 카운트
    graph[x][y] = 0

    # 2. 상하좌우 좌표계산
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if graph[nx][ny] == 1:
            dfs(nx, ny)


if __name__ == '__main__':
    T = int(input())

    while (T):
        cnt = 0
        T -= 1
        M, N, K = map(int, input().split())
        graph = []

        # M x N 만큼 행렬 만들기
        for i in range(N):
            temp = [0 for _ in range(M)]
            graph.append(temp)

        # print(graph)

        for i in range(K):
            y, x = map(int, input().split())
            graph[x][y] = 1

        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    dfs(i, j)
                    cnt += 1

        print(cnt)
