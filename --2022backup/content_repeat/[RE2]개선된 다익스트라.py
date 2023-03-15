import sys
import heapq


N, M = map(int, input().split())
start = int(input().rstrip())
INF = int(1e9)

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

# step1. 모든 간선 입력받기
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

# step2. 다익스트라
def dijkstra(start):
    q = []

    # 1) 출발지점 기준으로 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 2) 큐 탐색
    while q:
        # 거리가 가장 짧은 노드 꺼냄
        dist, now = heapq.heappop(q)

        # 해당 노드를 이미 처리했는지 확인
        if distance[now] < dist:    # 이미 갱신된 상태
            continue

        # 인접노드까지 가는 방향 모두 탐색  (해당 노드를 거쳐가기 위해)
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:   # 더 빠른경우
                distance[i[0]] = cost   # 비용갱신
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


