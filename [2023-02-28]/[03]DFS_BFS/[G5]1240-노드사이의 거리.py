import sys
from collections import deque
from collections import defaultdict,deque

input = sys.stdin.readline

N, M = map(int, input().split())
# graph = [list() for _ in range(N + 1)]
graph = defaultdict(list)


def bfs(start, end):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque()
    q.append(start)
    target_d = [0] * (N + 1)

    while q:
        v = q.popleft()

        if v == end:  # 도착지
            print(target_d[v])  # 저장된 내용 출력
            return

        for next, dist in graph[v]:
            if not visited[next]:  # 방문한 적이 없다면
                q.append(next)  # 가서 방문하도록 큐에 추가
                visited[next] = True
                # 다음 노드 거리 = 현재 노드 거리 + dist
                target_d[next] += target_d[v] + dist


for _ in range(N - 1):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])
    graph[b].append([a, d])

for _ in range(M):
    a, b = map(int, input().split())
    bfs(a, b)
