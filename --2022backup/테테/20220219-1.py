import sys
from collections import Counter

input = sys.stdin.readline


def logic(arr):
    result = []

    for k, v in sorted(Counter(arr).items()):
        if v == 1:
            result.append(k)

    if len(result) == 0:
        return [-1]
    else:
        return result


print(logic([2, 1, 3, 3]))
print(logic([3, 4, 4, 2, 5, 2, 5, 5]))
print(logic([3, 5, 3, 5, 7, 5, 7]))
