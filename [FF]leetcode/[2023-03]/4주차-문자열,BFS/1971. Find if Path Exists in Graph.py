from collections import deque
from typing import List

visited = []
graph = []


def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()

        if v == end:
            return True

        for d in graph[v]:
            if not visited[d]:
                visited[d] = True
                q.append(d)

    return False


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        global graph, visited
        graph = [deque() for _ in range(n)]
        visited = [False] * n

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        return bfs(source, destination)
