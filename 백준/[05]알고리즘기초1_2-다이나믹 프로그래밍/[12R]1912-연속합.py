import sys

N = int(input())
lst = list(map(int, input().split()))
dp = [0] * N
dp[0] = lst[0]

for i in range(1, N):
    # print(dp)
    dp[i] = max(lst[i], dp[i-1] + lst[i])  # 한번 더 체크를 위해 lst[i]를 사용

print(max(dp))


