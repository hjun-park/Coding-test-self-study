import sys

n, m = map(int, input().split())
max_value = -1

for _ in range(n):
    numbers = list(map(int, input().split()))

    tmp = min(numbers)
    if max_value < tmp:
        max_value = tmp

print(max_value)


