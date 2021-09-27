import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def D(n):
    return (2 * n) % 10000


def S(n):
    if not n - 1:
        return 9999
    else:
        return n - 1


def L(n):
    temp = list(map(int, str(n)))
    print(temp)
    head = temp[0]
    body = temp[1:]
    print(body, head)
    return int(''.join(body + [head]))


def R(n):
    temp = list(map(int, str(n)))
    print(temp)
    tail = temp[-1]
    body = temp[:-1]
    return int(tail + body)


def bfs(n):
    q = deque()
    q.append(n)

    while q:
        n = q.popleft()

        if n == B:
            return

        q.append(D(n))
        q.append(S(n))
        q.append(L(n))
        q.append(R(n))


for _ in range(T):
    # A: 레지스터 초기
    # B: 결과
    A, B = map(int, input().split())
    bfs(A)
    print("done")
