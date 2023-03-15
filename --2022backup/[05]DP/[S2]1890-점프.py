import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if graph[x][y] == 0:
            break
        nx = x + graph[x][y]
        ny = y + graph[x][y]

        if 0 <= nx < N:  # 범위 내에 있으면 nx혹은 ny에 이전값(graph[x][y])를 더함
            dp[nx][y] += dp[x][y]
        if 0 <= ny < N:
            dp[x][ny] += dp[x][y]

print(dp[-1][-1])
