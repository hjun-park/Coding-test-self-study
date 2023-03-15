import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []


def func(k):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(k, N + 1):
        arr.append(i)
        func(i)
        arr.pop()


func(1)
