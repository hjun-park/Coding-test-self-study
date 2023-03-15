import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(set(list(map(int, input().split())))))
N = len(nums)
arr = []


def logic():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        arr.append(nums[i])
        logic()
        arr.pop()


logic()
