import sys

sys.setrecursionlimit(100000)

N = int(input())


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(N))
