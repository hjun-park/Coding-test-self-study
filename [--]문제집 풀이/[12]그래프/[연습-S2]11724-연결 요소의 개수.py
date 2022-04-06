import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0


def bfs(e):
    global visited
    q = deque()
    q.append(e)
    visited[e] = True

    while q:
        v = q.popleft()

        for elem in graph[v]:
            if not visited[elem]:
                visited[elem] = True
                q.append(elem)


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
