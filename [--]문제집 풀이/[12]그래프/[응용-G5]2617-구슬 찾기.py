import sys
from collections import deque

input = sys.stdin.readline

# direct graph ?

N, M = map(int, input().split())  # 구슬 개수, 무게측정 개수

heavy_graph = [[] for _ in range(N+1)]
light_graph = [[] for _ in range(N+1)]

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        q.popleft()



for _ in range(M):
    a, b = map(int, input().split())

    heavy_graph[a].append(b)
    light_graph[b].append(a)

print(heavy_graph)  # 무거운것 --> 가벼운 것
print(light_graph)  # 가벼운 것 --> 무거운 것


# 끝을 찾기
for i in range(1, N+1):
    if heavy_graph[i]:
        bfs(i)

