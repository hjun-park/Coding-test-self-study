# -*- coding: utf-8 -*-
'''
    DFS : 모든 노드를 탐색해서 개수를 셀 때 유용
        - 스택을 사용, 재귀와 함께 구현
    DFS_BFS : 최단 거리, 최단 경로를 구할 때 유용
        - 큐를 사용, deque를 이용해 구현
'''
from collections import deque


# DFS: 입력 -> 우선 방문처리 + 출력 -> 해당 인접리스트에 있는 내역 loop 돌면서 방문하지 않았다면 => 재귀로 방문처리
# BFS: 입력 -> 시작지로 큐 생성 -> 현재 노드 방문처리 -> 큐가 빌 때까지 순환
#                                               -> 큐에서 원소를 뽑아 출력 -> 해당 원소 인접리스트 루프 돌면서 방문 X 노드 찾음
#                                               -> 찾으면 queue에 집어넣고 방문처리

def dfs(graph, v, visited):
    visited[v] = True  # 재귀함수 시작이면 방문처리
    print(v, end=' ')

    # 인접리스트 내역 loop 돌기
    for i in graph[v]:
        if not visited[i]:  # 만약 방문하지 않았다면
            dfs(graph, i, visited)  # 재귀 방문처리


def bfs(graph, start, visited):
    queue = deque([start])  # 시작지 큐 생성
    visited[start] = True  # 큐에 집어넣으면 방문처리

    while queue:  # 큐가 빌 때까지 순환
        v = queue.popleft()  # 큐에서 원소를 뽑아서
        print(v, end=' ')  # 출력

        # 해당 원소 인접 리스트 돌면서 방문하지 않은 노드 찾기
        for i in graph[v]:
            if not visited[i]:  # 만약 방문하지 않았다면
                queue.append(i)  # 큐에 집어넣는다.
                visited[i] = True   # 큐에 집어넣으면 무조건 방문처리


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

print('\n')

visited = [False] * 9

bfs(graph, 1, visited)


