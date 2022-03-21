import sys
import math

input = sys.stdin.readline


def solution(num):
    count = 0

    # num이 1인 경우도 있음
    if num == 1:
        return 0

    while True:
        num = num // 2 if num % 2 == 0 else (num * 3) + 1

        count += 1

        if num == 1:
            return count
        elif count == 500:
            return -1
