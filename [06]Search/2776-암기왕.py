import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    one = set(map(int, input().split()))
    M = int(input().rstrip())
    two = list(map(int, input().split()))

    for num in two:
        if num in one:
            print(1)
        else:
            print(0)
