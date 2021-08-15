import sys
from collections import Counter

stack = []
N = int(input())
s = list(map(int, sys.stdin.readline().split()))
cnt = Counter(s)

result = [-1 for _ in range(N)]

for i in range(N):
    # while stack and cnt[s[stack[-1]]] < cnt[s[i]]:
    while stack and cnt[stack[-1][0]] < cnt[s[i]]:
        # print(type(s[stack[-1]]))
        result[stack[-1][1]] = s[i]
        stack.pop()

    stack.append([s[i], i])

print(*result)
