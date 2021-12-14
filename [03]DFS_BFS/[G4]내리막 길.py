import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

'''
  [DFS + DP]
  * DFS + DP를 이용한 문제 길찾기의 경우 역으로도 접근하는 방법이 있다.
  https://seoyoung2.github.io/algorithm/2020/06/25/Baekjoon-1520.html
  
  1) DP 배열을 선언하고 -1로 초기화한다.
  2) DFS를 시작한다
    2-1) 만약 첫 번째 좌표에 도착했다면 길을 찾았으므로 1을 리턴한다.
    2-2) 만약 dp 배열 좌표값이 -1이라면 로직을 수행한다. 아닐 시 넘어간다.
      2-2-1) dp 배열을 0으로 초기화한다 ( 방문했으니 )
      2-2-2) nx, ny를 결정하고 체크한다 (역으로 순회하는거니까 다음 위치 값이 더 커야한다)
      2-2-3) 해당 길로 갈 수 있는 경우는 그 다음값으로 재귀함수를 타게 한다.
'''

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

# 1)
dp = [[-1] * N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    # 2-1)
    if x == 0 and y == 0:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[x][y] < graph[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(M - 1, N - 1))
