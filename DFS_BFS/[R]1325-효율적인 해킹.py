import sys
from collections import deque, defaultdict


# BFS
def bfs(graph, start):
    count = 1
    # 해당 문제에는 모든 N에 대해 방문을 할 것이므로 방문 시마다 초기화
    visited = [False] * (N + 1)
    visited[start] = True

    queue = deque([start])

    # 집어넣고 시작
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count


N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)

results = []
max_count = 0

for i in range(1, N + 1):
    count = bfs(graph, i)

    if max_count < count:
        max_count = count
    results.append([i, count])

for i, count in results:
    if count == max_count:
        print(i, end=' ')

'''
 1. n, m 입력받음
 2. bfs하기 위해 defaultdict(list) 생성
 3. A-B 관계 입력받은 후 역방향 연관관계 매핑
 4. 
'''

# ============================================
# 시간초과
# ============================================

# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(graph, v, visited):
#     global count
#     count += 1
#     # 1) 방문처리
#     visited[v] = True
#
#     # 2) v와 인접한 리스트 순회
#     for i in graph[v]:
#         # 만약 방문하지 않았다면 재귀로 순환 시작
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#
# N, M = map(int, sys.stdin.readline().split())
# graph = [[0] for _ in range(N+1)]
# count_list = []
# count = 0
#
# for _ in range(M):
#     A, B = map(int, sys.stdin.readline().split())
#     graph[B].append(A) # 단방향 관계로만 설정 ( 신뢰관계가 역이기 때문에 역으로 설정 )
#
# for i in range(1, N+1):
#     # if not visited[i]:
#     count = 0
#     visited = [False] * (N + 1)
#     dfs(graph, i, visited)
#     count_list.append(count)
#
# max_value = max(count_list)
#
# for i, num in enumerate(count_list):
#     if num == max_value:
#         print(i+1, end=' ')
#
