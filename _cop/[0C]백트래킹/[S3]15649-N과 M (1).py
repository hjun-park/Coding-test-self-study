import sys

input = sys.stdin.readline

N, M = map(int, input().split())

is_used = [False] * (N + 1)
arr = [0 for _ in range(M)]


def logic(k):
    # base condition
    if k == M:
        print(' '.join(map(str, arr)))
        return

    # recursion logic
    for i in range(1, N + 1):
        if not is_used[i]:
            arr[k] = i
            is_used[i] = True
            logic(k + 1)
            is_used[i] = False


logic(0)
