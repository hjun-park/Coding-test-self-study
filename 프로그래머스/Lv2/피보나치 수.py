import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dp = [0] * (int(1e5) + 1)


def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    elif dp[n] != 0:
        return dp[n]

    else:
        dp[n] = (solution(n - 1) + solution(n - 2)) % 1234567
        return dp[n]


print(solution(100000))
