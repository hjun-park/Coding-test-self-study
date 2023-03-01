import sys
from typing import List

input = sys.stdin.readline


def func(s: str, _dict: List):
    visited = [False] * len(s)

    for i in range(len(s)):
        for word in _dict:
            if s.startswith(word, i):
                for j in range(len(word)):
                    visited[j + i] = True

    rst = ''

    i = 0
    while i < len(s):
        if not visited[i]:
            rst += s[i]
            i += 1
            continue

        rst += '<b>'
        while i < len(s) and visited[i]:
            rst += s[i]
            i += 1

        rst += '</b>'

    return rst


print(func('abcxyz123', ['abc', '123']))
print(func('abcxyz123', ['abc', 'xyz']))
print(func('aaabbcc', ['aaa', 'aab', 'bc']))
print(func('aaabbccaabc', ['aaa', 'aab', 'bc']))
