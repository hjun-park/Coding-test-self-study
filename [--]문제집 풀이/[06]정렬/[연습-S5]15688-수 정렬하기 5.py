import sys

input = sys.stdin.readline

N = int(input().rstrip())
result = sorted([-int(input().rstrip()) for _ in range(N)], reverse=True)

for n in result:
    print(n*-1)
