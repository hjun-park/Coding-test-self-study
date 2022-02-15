import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0 for _ in range(M)]


def logic(k):
    if k == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, N + 1):
        arr[k] = i
        logic(k + 1)
        arr[k] = 0


logic(0)
