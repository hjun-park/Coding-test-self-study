import sys

input = sys.stdin.readline

N = int(input().rstrip())
for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * i)
