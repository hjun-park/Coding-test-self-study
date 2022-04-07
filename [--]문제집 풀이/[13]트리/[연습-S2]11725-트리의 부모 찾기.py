import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input().rstrip())

# 트리의 루트 1
# 각 노드의 부모 구하는 프로그램
graph = defaultdict(list)
parents = [0 for _ in range(N + 1)]


def bfs(start):
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()

        for e in graph[v]:
            if not parents[e]:
                parents[e] = v  # 부모 지정
                q.append(e)


root = 1
for _ in range(N - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

# tree는 전부 연결된 그래프이므로 for문으로 노드를 막 돌아주 필요가 없다.
bfs(1)  # 1번 부모부터 시작

for row in parents[2:]:
    print(row)
