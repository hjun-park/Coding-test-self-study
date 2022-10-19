import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    n, nums = nums[0], nums[1:]

    for _li in list(combinations(nums, 6)):
        print(*_li)

    print()


