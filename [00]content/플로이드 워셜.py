# 플로이드 워셜: DP 문제

"""
다익스트라 알고리즘
 - 한 정점에서 모든 정점까지의 거리를 알고 싶을때 사용

플로이드워셜 알고리즘
 - 모든 정점에서 모든 정점까지의 거리를 알고 싶을때 사용


결론:
 - 음의 가중치를 가지거나 모든 지점에서의 모든 최단거리를 구해야 한다면 => 플로이드 워셜 알고리즘
 - 하나의 정점을 가지고 다른 모든 정점까지의 최단거리를 구해야 한다. => 다익스트라 알고리즘
"""

import sys

INF = int(1e9)  # 무한

# 노드의 개수 및 간선 개수 입력
n = int(input())  # 노드
m = int(input())  # 간선

# 2차원 리스트(그래프 표현) 만든 후 모두 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 노드의 개수만큼 그래프 표현

print(graph)

# 자기 자신 => 자기 자신으로 가는 cost는 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력받아 그 값으로 초기화
for _ in range(m):
    # A => B 가는 경로의 비용은 C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따른 플로이드 워셜 알고리즘 수행
# a, b는 좌표, k는 거쳐가는 좌표 (빅오: O(n^3))
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한 INF 라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        # 도달할 수 있는 경우 거리 출력
        else:
            print(graph[a][b], end=' ')

    print()
