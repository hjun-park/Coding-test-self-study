import sys

input = sys.stdin.readline

n = int(input().rstrip())
key = n

cycle = 0
while True:
    cycle += 1
    _sum = n // 10 + n % 10
    n = n % 10 * 10 + _sum % 10
    if n == key:
        break
print(cycle)
