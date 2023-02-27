import sys
from typing import List

input = sys.stdin.readline


def func(s: str, _dict: List):
    visited = [False] * len(s)

    for d in _dict:
        start_idx = 0
        while True:
            idx = s.find(d, start_idx)
            if idx == -1:
                break

            visited[idx:idx+len(d)] = [True] * len(d)
            start_idx = idx + 1

    rst = ''
    before = False
    for i in range(len(visited)):
        if not before and visited[i]:    #
            rst += f'<b>{s[i]}'
            before = visited[i]

        elif before and not visited[i]:
            rst += f'</b>{s[i]}'
            before = visited[i]

        else:
            rst += s[i]
            before = visited[i]

    if visited[-1] is True:
        rst += '</b>'

    return rst


print(func('abcxyz123', ['abc', '123']))
print(func('abcxyz123', ['abc', 'xyz']))
print(func('aaabbcc', ['aaa', 'aab', 'bc']))
print(func('aaabbccaabc', ['aaa', 'aab', 'bc']))
