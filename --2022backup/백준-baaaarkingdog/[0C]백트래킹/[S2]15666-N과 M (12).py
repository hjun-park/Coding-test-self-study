import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(set(list(map(int, input().split())))))
N = len(nums)
arr = []


def logic(start):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(start, N):
        arr.append(nums[i])
        logic(i)
        arr.pop()


logic(0)
