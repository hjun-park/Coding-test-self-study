import itertools
import sys

input = sys.stdin.readline


def solution(v):
    _max = -1
    for li in list(itertools.permutations(v, len(v))):
        _sum = 0
        for i in range(len(li) - 1):
            _sum += abs(li[i] - li[i + 1])

        if _max < _sum:
            _max = _sum

    return _max


# def solution(v):
#     v = sorted(v)
#     nums = deque()
#
#     i = 0
#     while v:
#         if i % 2 == 0:
#             nums.appendleft(v.pop(-1))
#             nums.append(v.pop(0))
#         else:
#             nums.appendleft(v.pop(0))
#             nums.append(v.pop(-1))
#
#         i += 1
#
#     _sum = 0
#     for i in range(len(nums)-1):
#         _sum += abs(nums[i]-nums[i+1])
#
#     return _sum


print(solution([20, 8, 10, 1, 4, 15]))
print(solution([1, 1, 1, 1, 1, 1, 1]))
