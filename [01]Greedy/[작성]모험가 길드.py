import sys

n = int(input())
p = sorted(list(map(int, sys.stdin.readline().split())))

group = 0
for i in range(n):
    i += p[i] - 1
    print(i)
    group += 1

print(group)
