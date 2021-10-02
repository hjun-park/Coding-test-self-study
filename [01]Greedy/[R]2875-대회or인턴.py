import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

while K != 0:
    if N > M*2:
        N -= 1
        K -= 1
    else:
        M -= 1
        K -= 1

print(min(N//2, M))
