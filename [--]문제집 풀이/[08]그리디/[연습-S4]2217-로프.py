import sys

input = sys.stdin.readline

total = 0
weights = sorted([int(input().rstrip()) for _ in range(int(input().rstrip()))], reverse=True)

for i in range(1, len(weights) + 1):
    weights[i - 1] = weights[i - 1] * i

print(max(weights))
