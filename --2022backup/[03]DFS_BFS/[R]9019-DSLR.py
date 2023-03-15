import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def D(n):
    res = n * 2
    if res > 9999:
        res %= 10000
    return res


def S(n):
    res = n
    if res == 0: return 9999
    res -= 1
    return res


def L(n):
    div = n // 1000
    remain = n % 1000

    return remain * 10 + div


def R(n):
    div = n // 10
    remain = n % 10

    return remain * 1000 + div


def bfs(n):
    q = deque()
    visited = set()  # log(n)    # 중복되는 숫자는 방문하지 않도록 설정
    q.append((n, ''))
    visited.add(n)

    while q:
        n, commands = q.popleft()

        if n == B:
            print(commands)
            return

        # 미리 계산해 보고 이미 결과로 나왔던 값인지 확인
        tmp = D(n)
        if tmp not in visited:  # 나오지 않았다면 방문 등록 후 q 추가
            visited.add(tmp)
            q.append((tmp, commands + "D"))

        tmp = S(n)
        if tmp not in visited:  # 나오지 않았다면 방문 등록 후 q 추가
            visited.add(tmp)
            q.append((tmp, commands + "S"))

        tmp = L(n)
        if tmp not in visited:  # 나오지 않았다면 방문 등록 후 q 추가
            visited.add(tmp)
            q.append((tmp, commands + "L"))

        tmp = R(n)
        if tmp not in visited:  # 나오지 않았다면 방문 등록 후 q 추가
            visited.add(tmp)
            q.append((tmp, commands + "R"))


for _ in range(T):
    # A: 레지스터 초기
    # B: 결과
    A, B = map(int, input().split())
    bfs(A)
