import sys
import heapq
'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
input = sys.stdin.readline

# 필요한 변수 [입력]
# a) 노드의 개수 간선 [입력]
N, M = map(int, input().split())
# b) 시작 노드 번호 [입력]
start = int(input().rstrip())

# 필요한 변수 [고정]
# a) 그래프 [입력]
graph = [[] for i in range(N + 1)]
# b) INF = int(1e9)
INF = int(1e9)
# d) 최단거리 distance = [INF] * (n + 1)
distance = [INF] * (N + 1)

# step1. 모든 간선 입력받기
for _ in range(M):
    a, b, c = map(int, input().split())
    # a -> b로 가는 비용이 c라는 의미
    graph[a].append([b, c])


# step2. 다익스트라 루프
def dijkstra(start):
    q = []

    # 1) 출발노드를 설정하고 큐에 넣기
    heapq.heappush(q, (0, start))   # (최단거리, 좌표)
    distance[start] = 0

    while q:
        # 2) 거리가 가장 짧은 노드를 꺼내서 확인
        dist, now = heapq.heappop(q)    # 거리, 현재위치

        # 3-1) 이미 짧은 거리로 갱신이 된 상태라면 갱신할 필요가 없음
        if distance[now] < dist:
            continue

        # 4) 갱신이 필요하다면 현재위치와 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]  # 이전 거리 + 현재 노드까지의 거리

            if cost < distance[i[0]]:    # 기존 경로보다 더 짧다면
                distance[i[0]] = cost   # 거리 갱신
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# step3. 모든 노드로 가기 위한 최단 거리 출력
#   - 도달할 수 없는 경우에는 INFINITY라고 출력
#   - 도달할 수 있는 경우에는 거리 출력
for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
