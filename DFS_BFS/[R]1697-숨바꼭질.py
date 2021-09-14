import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001
time = [0] * MAX


def bfs(start, target):
    queue = deque()
    queue.append(start)

    while queue:
        X = queue.popleft()

        if X == target:
            print(time[X])
            return

        for nx in (X + 1, X - 1, 2 * X):
            # nx는 MAX값보다 작고 시간값도 비어있다면
            if 0 <= nx < MAX and not time[nx]:
                time[nx] = time[X] + 1
                queue.append(nx)


bfs(N, K)
