import sys

input = sys.stdin.readline

N = int(input().rstrip())
num = 1
while num*(num+1) / 2 <= N:
    num += 1
print(num - 1)

