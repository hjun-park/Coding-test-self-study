import sys

input = sys.stdin.readline

arr = []


def func(k, n):
    if len(arr) == 6:
        print(*arr)
        return

    for i in range(k, n):
        arr.append(nums[i])
        func(i + 1, n)
        arr.pop()


while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    N, nums = nums[0], nums[1:]

    func(0, N)

    print()
