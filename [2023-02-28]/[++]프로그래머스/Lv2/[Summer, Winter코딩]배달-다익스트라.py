# 다익스트라 알고리즘

import heapq

INF = int(1e9)


# step2. 다익스트라 루프
def dijkstra(start, graph, distance):
    q = []

    # 1) 출발노드를 설정하고 큐에 넣기
    heapq.heappush(q, (0, start))  # (최단거리, 좌표)
    distance[start] = 0

    while q:
        # 2) 거리가 가장 짧은 노드를 꺼내서 확인
        dist, now = heapq.heappop(q)  # 거리, 현재위치

        # 3-1) 이미 짧은 거리로 갱신이 된 상태라면 갱신할 필요가 없음
        if distance[now] < dist:
            continue

        # 4) 갱신이 필요하다면 현재위치와 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]  # 이전 거리 + 현재 노드까지의 거리

            if cost < distance[i[0]]:  # 기존 경로보다 더 짧다면
                distance[i[0]] = cost  # 거리 갱신
                heapq.heappush(q, (cost, i[0]))


def solution(N, road, K):
    # 필요한 변수 [고정]
    # a) 그래프 [입력]
    graph = [[] for _ in range(N + 1)]

    # d) 최단거리 리스트 초기화 = [INF] * (n + 1)
    distance = [INF] * (N + 1)

    # step1. 모든 간선 입력받기
    for r in road:
        a, b, c = r[0], r[1], r[2]
        # a -> b로 가는 비용이 c라는 의미
        # if graph[a][1] < c:
        #     continue

        graph[a].append([b, c])
        graph[b].append([a, c])

    # 1부터 시작하는 모든 경로 구함
    dijkstra(1, graph, distance)

    cnt = 0
    for d in distance:
        if d <= K:
            cnt += 1

    return cnt


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
