import sys

input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


t = int(input())

for _ in range(t):
    total = 0
    case = list(map(int, input().split()))
    n = case[0]
    numbers = case[1:]

    for i in range(n):
        for j in range(i + 1, n):
            gcd_num = gcd(numbers[i], numbers[j])
            total += gcd_num

    print(total)
