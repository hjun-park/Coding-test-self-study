import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())  # 친구
M = int(input().rstrip())  # 줄 길이

graph = [[] for _ in range(N + 1)]


def bfs(start):
    count = 0
    visited = [False] * (N + 1)
    visited[start] = True

    q = deque()
    q.append((start, 0))  # 시작 좌표와 친구 수

    while q:
        x, distance = q.popleft()

        # 친구의 친구까지만 초대가 가능한 점, 그래서 2이하로 제한
        if distance <= 2:
            count += 1

        # 인접한 노드를 탐색
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                q.append((v, distance + 1))
    return count - 1


for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))
