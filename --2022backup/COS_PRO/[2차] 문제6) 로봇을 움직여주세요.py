# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(commands):
    answer = []
    _dict = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    x, y = 0, 0

    for c in list(commands):
        dx, dy = _dict[c]
        x += dx
        y += dy

    return [x, y]


commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은", ret, "입니다.")
