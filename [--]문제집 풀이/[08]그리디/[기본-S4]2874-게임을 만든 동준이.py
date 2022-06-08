import sys

input = sys.stdin.readline

N = int(input().rstrip())
levels = list(reversed([int(input().rstrip()) for _ in range(N)]))
cnt = 0

for i in range(N - 1):
    if levels[i] > levels[i + 1]:
        continue
    else:
        tmp = levels[i + 1] - (levels[i] - 1)
        cnt += tmp
        levels[i + 1] -= tmp

print(cnt)
