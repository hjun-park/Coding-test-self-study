# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from itertools import combinations


def solution(arr, K):
    answer = 0

    for combi in list(combinations(arr, 3)):
        if sum(combi) % 3 == 0:
            answer += 1

    return answer


arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")
