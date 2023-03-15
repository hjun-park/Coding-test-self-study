import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = int(1e5 + 1)
time = [0] * MAX
path = [0] * MAX


def bfs(start, target):
    queue = deque()
    queue.append(start)

    while queue:
        X = queue.popleft()

        if X == target:
            print(time[X])
            p = []
            while X != start:
                p.append(X)
                X = path[X]  # 뽑아져나오는 X는 이전 좌표

            p.append(start)  # 위 반복에서 start와 같다면 종료이므로 따로 추가
            p.reverse()
            print(' '.join(map(str, p)))

            return

        for nx in (X - 1, X + 1, 2 * X):
            if 0 <= nx < MAX and not time[nx]:
                time[nx] = time[X] + 1
                path[nx] = X
                queue.append(nx)


bfs(N, K)
