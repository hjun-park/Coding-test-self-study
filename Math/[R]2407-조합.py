import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def factorial(n):
    res = 1
    for i in range(n):
        res *= (i + 1)
    return res


if m > (n // 2):
    m = n - m

print(factorial(n) // (factorial(m) * factorial(n - m)))
