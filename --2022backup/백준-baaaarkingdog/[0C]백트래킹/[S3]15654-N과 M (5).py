import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
is_used = [False] * (N + 1)
arr = []


def func():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        if not is_used[i]:
            is_used[i] = True
            arr.append(nums[i])
            func()
            arr.pop()
            is_used[i] = False


func()
