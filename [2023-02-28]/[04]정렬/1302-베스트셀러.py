import sys
from collections import Counter

input = sys.stdin.readline

N = int(input().rstrip())
title = []

for _ in range(N):
    title.append(input().rstrip())

title.sort()

title = Counter(title).most_common()

print(title[0][0])
