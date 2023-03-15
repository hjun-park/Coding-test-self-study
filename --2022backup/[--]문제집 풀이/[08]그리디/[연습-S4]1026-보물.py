import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

total = 0
for i in range(N):
    total += A[i] * B[i]

print(total)
