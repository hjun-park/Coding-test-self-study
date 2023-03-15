# NM(2)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
is_used = [False] * (N + 1)
arr = [0 for _ in range(M)]


def func(k):
    if k == M:
        print(' '.join(map(str, arr)))
        return

    start = 1  # 시작지점 존재
    if k != 0:
        start = arr[k - 1] + 1

    for i in range(start, N + 1):
        if not is_used[i]:
            arr[k] = i
            is_used[i] = True
            func(k + 1)
            is_used[i] = False


func(0)
