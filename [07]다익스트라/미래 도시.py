import sys

INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현) 만든 후 모든 값 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자신으로 가는 비용 0
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력 및 초기화
for _ in range(m):
    # A <-> B 서로 가는 비용 1이라 가정 ( 왜 1이라 가정 ? )
    # 문제에서는 연결된 모든 거리는 1마하라고 지정했기 때문,
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지인 K 입력
# 문제에서는 1에서 출발하여 소개팅 대상이 있는 회사 K를 거쳐 물품을 판매할 회사 X가 최종 목적지
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행 (빅오: O(n^3))
# k를 거쳐가는 좌표 [a][b]를 전부 찾는 것이므로 빅오 O(n^3)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력 ( 1 => k => x )
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")

# 도달할 수 있는 경우 최단 거리 출력
else:
    print(distance)
