import sys
from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    print(lcm(a, b))

