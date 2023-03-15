import sys

input = sys.stdin.readline

# direct graph ?

N, M = map(int, input().split())  # 구슬 개수, 무게측정 개수

heavy_graph = [[] for _ in range(N + 1)]
light_graph = [[] for _ in range(N + 1)]


# DFS 예제 :: 재귀를 이용하여 해결
def dfs_example(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:  # [2, 3, 8] :: i = 2 // 인접리스트 가장 첫 번째 요소의 가장 우선순위 높은 값 지정
        if not visited[i]:  # [1, 7] // 해당 인접리스트와 연결된 부분
            dfs(graph, i, visited)


pass_cnt = 0


def dfs(start, graph):
    global pass_cnt
    visited[start] = True

    for e in graph[start]:
        if not visited[e]:
            pass_cnt += 1
            dfs(e, graph)

    return pass_cnt


for _ in range(M):
    a, b = map(int, input().split())

    heavy_graph[a].append(b)
    light_graph[b].append(a)

# print(heavy_graph)  # 무거운것 --> 가벼운 것
# print(light_graph)  # 가벼운 것 --> 무거운 것

# 중앙값 설정 (구슬 갯수의 중앙값)
median = (N + 1) // 2

# 끝을 찾기
cnt = 0
for i in range(1, N + 1):
    visited = [False] * (N + 1)

    # 
    if dfs(i, heavy_graph) >= median:
        cnt += 1
    pass_cnt = 0
    if dfs(i, light_graph) >= median:
        cnt += 1
    pass_cnt = 0

print(cnt)
