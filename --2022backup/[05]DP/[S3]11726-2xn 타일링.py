import sys

# bottom-up(반복문 이용하는 타뷸레이션)
input = sys.stdin.readline

MOD = 10_007  # (_)는 자리구분용으로 씀
N = int(input().rstrip())
dp = [-1] * (N + 1)

dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[N])
