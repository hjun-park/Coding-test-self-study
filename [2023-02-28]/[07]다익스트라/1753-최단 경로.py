import heapq
import sys

input = sys.stdin.readline

# v = 접점, E=간선
V, E = map(int, input().split())
start = int(input().rstrip())

INF = int(1e9)
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

# 간선 입력
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        # 이미 갱신되었는지 확인 (방문확인)
        if distance[now] < dist:
            continue

        # 갱신이 필요하면 모든 인접노드 탐색
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:  # 저렴한 비용의 새 경로가 있다면 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
