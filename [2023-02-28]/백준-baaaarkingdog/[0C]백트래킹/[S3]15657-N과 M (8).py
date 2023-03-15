import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = []


def func(k):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(k, N):
        arr.append(nums[i])
        func(i)
        arr.pop()


func(0)
