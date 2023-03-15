# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(arr):
    answer = 0

    _len = 1
    for i in range(1, len(arr)):
        for j in range(i, len(arr)):
            if arr[j - 1] < arr[j]:
                _len += 1
            else:
                answer = max(answer, _len)
                _len = 0
                break

    answer = max(answer, _len)

    return answer + 1
