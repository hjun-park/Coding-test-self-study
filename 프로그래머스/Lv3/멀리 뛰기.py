import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dp = [-1] * 2001


def fibo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif dp[x] != -1:
        return dp[x]

    dp[x] = fibo(x - 1) + fibo(x - 2)

    return dp[x] % 1234567


def solution(n):
    answer = fibo(n)
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
