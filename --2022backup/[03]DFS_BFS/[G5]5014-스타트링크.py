import sys
from collections import deque

input = sys.stdin.readline

# 최고층 / 현재위치 / 가고싶은 층 / 위 / 아래
F, S, G, U, D = map(int, input().split())


def bfs():
    visited = [False] * (F + 1)
    q = deque()
    q.append((S, 0))  # 현재 위치 대입

    while q:
        v, btn = q.popleft()

        if v == G:
            return btn

        for d in [U, D * (-1)]:
            nv = v + d

            if 1 <= nv <= F:
                if not visited[nv]:
                    visited[nv] = True
                    q.append((nv, btn + 1))

    return "use the stairs"


print(bfs())
