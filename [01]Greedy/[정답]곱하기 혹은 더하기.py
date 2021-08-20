import sys

numbers = list(map(int, sys.stdin.readline().rstrip()))
result = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] <= 1 or result <= 1:
        result += numbers[i]
    else:
        result *= numbers[i]

print(result)

