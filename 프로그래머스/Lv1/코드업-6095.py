import sys

input = sys.stdin.readline

h, w = map(int, input().split())
graph = [[0] * w for _ in range(h)]

for _ in range(int(input().rstrip())):
    l, d, x, y = map(int, input().split())

    if d != 0:
        for i in range(l):
            graph[x-1+i][y-1] = 1

    else:
        for j in range(l):
            graph[x-1][y-1+j] = 1

for row in graph:
    print(*row)
