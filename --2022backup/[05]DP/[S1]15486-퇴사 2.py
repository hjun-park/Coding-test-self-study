import sys

input = sys.stdin.readline

N = int(input().rstrip())

dp = [0] * 1_500_001

# 날짜 / 금액
days = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if i + days[i][0] <= N:  # 1) 일이 끝나는 날이 N일 이하라면 일이 가능함
        # max(기존 값, 이전까지의 페이 + 이번 일이 끝났을 때 페이)
        dp[i + days[i][0]] = max(dp[i + days[i][0]], dp[i] + days[i][1])

    # 자연스레 전날 값은 다음날에도 반영한다.
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[N])
