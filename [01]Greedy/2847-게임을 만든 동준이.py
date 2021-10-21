import sys

input = sys.stdin.readline

N = int(input().rstrip())
scores = []
for _ in range(N):
    scores.append(int(input().rstrip()))

'''
    가끔은 뒤집어서 생각해본다.
'''

cnt = 0
for i in range(N - 1, 0, -1):
    if scores[i] <= scores[i - 1]:
        cnt += (scores[i - 1] - scores[i] + 1)
        scores[i - 1] = scores[i] - 1

print(cnt)
