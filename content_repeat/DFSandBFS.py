import sys
from collections import deque

def bfs(graph, start, visited):
    # bfs는 즉시 방문처리하고 출력, 옆으로 이동
    visited[start] = True
    queue = deque([start])  # 지점 넣기

    # 큐를 순회하며 bfs
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        # 인접리스트 확인
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




def dfs(graph, v, visited):
    # 일단 방문처리 후 출력 ( 파고드는 형태 )
    visited[v] = True
    print(v, end = ' ')

    # 인접리스트 순회하면서 확인
    for i in graph[v]:
        if not visited[i]:  # 미방문지라면 재귀 이용하여 DFS
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
