import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = sorted(list(map(int, input().split())))
x = int(input().rstrip())

left, right = 0, n - 1

cnt = 0
while left < right:
    num = nums[left] + nums[right]

    if num == x:
        cnt += 1
        left += 1
    elif num > x:
        right -= 1
    else:
        left += 1

print(cnt)
