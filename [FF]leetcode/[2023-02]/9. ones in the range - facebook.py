import sys

input = sys.stdin.readline


def logic(arr, s, e):
    return sum(arr[s:e + 1])


print(logic([0, 0, 1, 0, 1], 2, 4))
print(logic([0, 1, 1, 0, 0, 1, 1, 1], 2, 6))
print(logic([0, 1, 1, 0, 0, 1, 1, 1], 1, 7))
