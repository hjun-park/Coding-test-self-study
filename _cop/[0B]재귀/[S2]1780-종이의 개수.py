import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

rst = defaultdict(int)


def func(n, r, c):
    base = graph[r][c]

    if n == 1:
        rst[base] += 1
        return

    half = n // 3
    for i in range(r, r + n):
        for j in range(c, c + n):
            if base != graph[i][j]:
                func(half, r, c)
                func(half, r, c + (n // 3))
                func(half, r, c + (n // 3 * 2))
                func(half, r + (n // 3), c)
                func(half, r + (n // 3), c + (n // 3))
                func(half, r + (n // 3), c + (n // 3 * 2))
                func(half, r + (n // 3 * 2), c)
                func(half, r + (n // 3 * 2), c + (n // 3))
                func(half, r + (n // 3 * 2), c + (n // 3 * 2))
                return

    rst[base] += 1


func(N, 0, 0)
print(rst[-1], rst[0], rst[1])
