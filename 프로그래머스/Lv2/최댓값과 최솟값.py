import sys

input = sys.stdin.readline


def solution(s):
    s_list = list(map(int, s.split()))

    return ' '.join(map(str, [min(s_list), max(s_list)]))


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
