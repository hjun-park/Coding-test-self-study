import sys

input = sys.stdin.readline

A, B = map(int, input().split())

numbers = []

for i in range(1, 1000):
    if len(numbers) >= B:
        break
    for j in range(i):
        numbers.append(i)
numbers = numbers[A - 1:B]

print(sum(numbers))
