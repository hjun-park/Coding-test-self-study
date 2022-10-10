import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(N)]


def func(n, r, c):
    base = graph[r][c]
    if n == 1:
        print(f'{base}', end='')
        return

    half = n >> 1
    for i in range(r, r + n):
        for j in range(c, c + n):
            if graph[i][j] != graph[r][c]:
                print('(', end='')
                func(half, r, c)
                func(half, r, c + half)
                func(half, r + half, c)
                func(half, r + half, c + half)
                print(')', end='')
                return

    print(f'{base}', end='')


func(N, 0, 0)
