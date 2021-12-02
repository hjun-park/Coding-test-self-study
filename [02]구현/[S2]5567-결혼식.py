import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


def bfs(start):
    count = 0
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        x, depth = q.popleft()

        if depth <= 2:
            count += 1

        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                q.append((v, depth + 1))

    return count - 1


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))
