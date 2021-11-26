import sys
from collections import deque
sys.setrecursionlimit(10000)

'''
 1) 전반적 형태
  - 입력값 ( N, M, graph, visited )
  - 좌표 입력 ( 간선은 한 쪽만 이어도 두 쪽이 연결됨 )
  - 정점은 0이 아닌 1부터 시작하기 때문에 for문 1부터 시작
  - 처음부터 해서 방문하지 않았다면 자연스레 dfs를 돌려주면 된다.
'''

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M = map(int, input().split())
graph = [[0] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)

# 정점은 1부터 시작함
count = 0
for i in range(1, N + 1):
    if not visited[i]:  # 방문하지 않았다면
        dfs(graph, i, visited)
        count += 1

print(count)


