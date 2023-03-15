def lcm(a, b):
    return (a * b) // gcd(a, b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(n, m):
    return [gcd(n, m), lcm(n, m)]
