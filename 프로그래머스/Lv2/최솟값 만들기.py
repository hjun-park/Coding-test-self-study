import sys

input = sys.stdin.readline


def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    result = 0
    for a, b in zip(A, B):
        result += a * b

    return result


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))
