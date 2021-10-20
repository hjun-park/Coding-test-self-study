import sys

input = sys.stdin.readline

numbers = list(map(int, input().rstrip()))

result = numbers[0]
for i in range(1, len(numbers)):
    if result > 1 and numbers[i] > 1:
        result *= numbers[i]
    else:
        result += numbers[i]

print(result)



