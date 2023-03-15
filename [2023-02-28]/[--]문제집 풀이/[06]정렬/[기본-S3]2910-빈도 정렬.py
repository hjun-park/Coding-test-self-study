import sys
from collections import Counter

input = sys.stdin.readline

N, C = map(int, input().split())
message = list(map(int, input().split()))

print(Counter(message))

for k, v in Counter(message).items():
    for _ in range(v):
        print(k, end=' ')
