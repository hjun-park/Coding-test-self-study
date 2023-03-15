import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    nums = list(map(str, input().split()))

    if nums.pop(0) == '0':
        break

    for i in combinations(nums, 6):
        print(" ".join(i))

    print()









