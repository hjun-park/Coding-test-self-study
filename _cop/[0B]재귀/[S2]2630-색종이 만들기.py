import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

_dict = defaultdict(int)


def func(n, r, c):
    base = graph[r][c]

    if n == 1:
        _dict[base] += 1
        return

    half = n >> 1
    for i in range(r, r + n):
        for j in range(c, c + n):
            if graph[i][j] != base:
                func(half, r, c)
                func(half, r, c + half)
                func(half, r + half, c)
                func(half, r + half, c + half)
                return

    _dict[base] += 1


func(N, 0, 0)
print(_dict[0])
print(_dict[1])
