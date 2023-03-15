import sys

input = sys.stdin.readline

N = int(input().rstrip())

expect = []
for _ in range(N):
    expect.append(int(input().rstrip()))

expect.sort()
result = 0
for i in range(len(expect)):
    result += abs(expect[i] - (i + 1))

print(result)
