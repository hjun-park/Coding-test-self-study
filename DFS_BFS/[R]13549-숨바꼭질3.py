import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = int(1e5 + 1)
time = [-1] * MAX


# https://jinho-study.tistory.com/1016

def bfs(start, target):
    queue = deque()
    queue.append(start)
    time[start] = 0

    while queue:
        X = queue.popleft()

        if X == target:
            return

        for nx in [X*2, X+1, X-1]:  # 이거 순서 하나때문에 맞고 틀릴 수 있음
            if 0 <= nx < MAX and time[nx] == -1:
                queue.append(nx)
                time[nx] = time[X] + (0 if nx == X*2 else 1)


bfs(N, K)
print(time[K])
