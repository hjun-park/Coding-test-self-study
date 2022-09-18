import sys

input = sys.stdin.readline

n = int(input().rstrip())

sequence = 0
for i in range(1, n + 1):
    nums = list(map(int, str(i)))  # 숫자 리스트화
    if i < 100:
        print(sequence)  # 100보다 작으면 모두 한수
        sys.exit(0)
    elif nums[0] - nums[1] == nums[1] - nums[2]:
        sequence += 1  # 1씩 차이나면 한수

print(sequence)
