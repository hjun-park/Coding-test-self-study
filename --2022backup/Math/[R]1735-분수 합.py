import sys

input = sys.stdin.readline

'''
    분자와 분모의 유클리드 호제법으로 GCD 구한 후
    각 GCD로 기약분수가 아닌 분자, 분모를 나누면 기약분수가 나옴
'''

nume1, deno1 = map(int, input().split())
nume2, deno2 = map(int, input().split())


def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod  # y는 나누어지는 수
        mod = x % y
    return y


# 분자와 분수의 최대공약수를 구함
nume = nume1 * deno2 + nume2 * deno1
deno = deno1 * deno2
num = gcd(nume, deno)
print(nume // num, deno // num)
