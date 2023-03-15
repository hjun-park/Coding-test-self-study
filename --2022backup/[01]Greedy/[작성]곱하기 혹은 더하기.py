import sys

# numbers = list(map(int, sys.stdin.readline().rstrip()))
# result = 0

# for num in numbers:
#     if result == 0 or num == 0 or num == 1:
#         result += num
#     else:
#         result *= num

# 모범답안
numbers = list(map(int, sys.stdin.readline().rstrip()))
result = numbers[0]

for i in range(1, len(numbers)):
    num = numbers[i]    # 더하거나 곱하려는 숫자

    # # 두 수중 하나라도 1이하면 더하고 2이상이면 곱한다.
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)


