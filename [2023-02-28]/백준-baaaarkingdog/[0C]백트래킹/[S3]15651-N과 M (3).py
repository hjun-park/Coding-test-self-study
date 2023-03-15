# NM(3)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0 for _ in range(M)]


def func(k):
    if k == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, N + 1):
        arr[k] = i
        func(k + 1)
        arr[k] = 0


func(0)
