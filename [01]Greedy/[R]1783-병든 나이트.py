import sys

input = sys.stdin.readline

move = [(-2, 1), (-1, 2), (1, 2), (2, 1)]

N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M + 1) // 2))
elif M < 7:
    print(min(4, M))
else:
    print(M - 7 + 5)
