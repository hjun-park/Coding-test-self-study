import sys


def cnt2(x):  # 2로 나눠지는 개수 카운트
    n2 = 0
    while x != 0:
        x //= 2
        n2 += x
    return n2


def cnt5(x):  # 5로 나눠지는 개수 카운트
    n5 = 0
    while x != 0:
        x //= 5
        n5 += x
    return n5


n, m = map(int, input().split())
print(min(cnt2(n) - cnt2(m) - cnt2(n - m), cnt5(n) - cnt5(m) - cnt5(n - m)))
