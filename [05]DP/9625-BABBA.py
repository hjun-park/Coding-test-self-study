import sys

'''
    A           1 0 = 1
    B A         1 1 = 2
    BA B        1 2 = 3
    BAB BA      2 3 = 5
'''
# 피보나치 형태
n = int(input())
d = [0] * (n + 1)


def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(f'{fibo(n - 1)} {fibo(n)}')
