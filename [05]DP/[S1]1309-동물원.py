import sys

input = sys.stdin.readline

N = int(input().rstrip())

dp = [[0, 0, 0] for _ in range(N + 1)]

'''
    dp[n][0] : n 줄에 사자를 하나도 배치하지 않고 만들 수 있는 최대 수
    dp[n][1] : n 줄에 1열에 사자 하나 놓고 배치할 수 있는 최대 수
    dp[n][2] : n 줄에 2열에 사자 하나 놓고 배치할 수 있는 최대 수
'''

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, N + 1):
    # dp[i][0]: i줄 0번째 index에 사자를 하나도 배치하지 않고 만드는 경우는,
    # i-1줄에 사자를 놓지않던, 다 놓던 어디든지 놓을 수 있다.
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[N]) % 9901)
