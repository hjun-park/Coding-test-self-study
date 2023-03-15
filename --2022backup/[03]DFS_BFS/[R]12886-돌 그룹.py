import sys
from collections import deque, defaultdict

input = sys.stdin.readline

stones = list(map(int, input().split()))
sum_stone = sum(stones)
visited = defaultdict(bool)

'''
    https://dirmathfl.tistory.com/179
'''


def bfs():
    # 합계가 돌 갯수로 나누어지는 경우는 답 도출 불가
    if sum_stone % 3 == 0:
        return 0

    q = deque([stones])
    visited[tuple(stones)] = True

    while q:
        a, b, c = q.popleft()
        if a == b == c:
            return 1

        for x, y in ((a, b), (a, c), (b, c)):
            if x == y:
                continue
            elif x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y

            # a, b는 구했으니 c를 구할 차례
            z = sum_stone - x - y

            if not visited[(x, y, z)]:
                visited[(x, y, z)] = True
                q.append([x, y, z])

    return 0


bfs()
