import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    temp = list(map(int, input().split()))
    k = temp[0]

    if k == 0:
        break

    nums = temp[1:]

    for li in list(combinations(nums, 6)):
        print(*li)

    print()
