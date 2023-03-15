import sys

input = sys.stdin.readline

S = input().rstrip()

before = S[0]
cnt0 = 0
cnt1 = 0
for i in range(1, len(S)):
    if before == S[i]:
        continue
    else:



