import sys

input = sys.stdin.readline


def solution(n):
    string_bin = format(n, 'b')

    n_count = string_bin.count('1')

    while True:
        n += 1
        string_bin = format(n, 'b')
        next_count = string_bin.count('1')

        if n_count == next_count:
            return n


print(solution(78))
print(solution(15))
