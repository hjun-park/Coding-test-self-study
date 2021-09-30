import sys
from collections import deque

input = sys.stdin.readline
MAX = 10e9

s, t = map(int, input().split())

check = set()
check.add(s)


def bfs(number):
    q = deque()
    q.append((number, ''))

    if s == t:
        return 0

    while q:
        num, op = q.popleft()

        if num == t:
            return op

        temp = num * num
        if 0 <= temp <= MAX and temp not in check:
            q.append((temp, op + '*'))
            check.add(temp)

        temp = num + num
        if 0 <= temp <= MAX and temp not in check:
            q.append((temp, op + '+'))
            check.add(temp)

        # 함정 같은 수를 더하거나 뺴도 0이고 0에서 0을 나누지도 못하고 골치아픈 존재
        # temp = num - num
        # if temp > 0:
        #     q.append((temp, op + '-'))

        # temp = num // num   # 같은 값을 나누니까 결국 1
        temp = 1
        if temp not in check:
            q.append((temp, op + '/'))
            check.add(temp)

    return -1


print(bfs(s))
