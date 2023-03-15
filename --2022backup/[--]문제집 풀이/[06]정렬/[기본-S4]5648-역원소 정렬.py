import sys

input = sys.stdin.readline

nums = []
nums2 = []
while True:
    temp = list(input().split())

    nums.extend(temp)

    if len(nums) == (int(nums[0]) + 1):
        break

n = int(nums.pop(0))

for num in nums:
    nums2.append(int(num[::-1]))

for num in sorted(nums2):
    print(num)
