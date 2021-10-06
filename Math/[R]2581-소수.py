import sys
from math import sqrt

input = sys.stdin.readline


def find_prime_number(M, N):
    array = [True for _ in range(N + 1)]
    array[0] = False
    array[1] = False

    for i in range(2, N + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1

    return [i for i in range(M, N + 1) if array[i]]


M = int(input().rstrip())
N = int(input().rstrip())

result = find_prime_number(M, N)
# print(result)

if result:
    print(f'{sum(result)}\n{min(result)}')
else:
    print(-1)

