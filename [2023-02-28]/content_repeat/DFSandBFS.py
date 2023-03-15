import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')   # 출력을 바로 하는 DFS와 다르게 BFS는 출력을 먼저 하지 않음

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v] = True

    # 인접리스트 확인
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 히스토리 리스트
visited = [False] * 9

# dfs 순환
dfs(graph, 1, visited)

print('\n')
visited = [False] * 9

bfs(graph, 1, visited)
