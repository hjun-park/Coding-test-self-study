# -*- coding: utf-8 -*-
'''
    DFS : 모든 노드를 탐색해서 개수를 셀 때 유용
        - 스택을 사용, 재귀와 함께 구현
    DFS_BFS : 최단 거리, 최단 경로를 구할 때 유용
        - 큐를 사용, deque를 이용해 구현
'''
from collections import deque


# DFS_BFS 예제 :: 큐를 이용하여 해결
def bfs(graph, start, visited):
    # 큐 구현 위해 deque 라이브러리 사용
    queue = deque([start])  # 첫 번째 시작값 deque에 집어넣고
    # 현재 노드 방문 처리
    visited[start] = True  # 방문처리
    # 큐가 빌 때까지 반복
    while queue:  # 큐가 빌 때까지 실행
        # 큐에서 하나의 원소를 뽑아서 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:  # v는 해당 원소와 인접한 부분
            if not visited[i]:  # 해당 원소 방문하지 않았다면
                queue.append(i) # 탐색할 대상에 집어넣음
                visited[i] = True   # 방문 처리


# DFS 예제 :: 재귀를 이용하여 해결
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:  # [2, 3, 8] :: i = 2 // 인접리스트 가장 첫 번째 요소의 가장 우선순위 높은 값 지정
        if not visited[i]:  # [1, 7] // 해당 인접리스트와 연결된 부분
            dfs(graph, i, visited)


if __name__ == '__main__':
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

    # 각 노드가 방문한 정보를 리스트로 표현
    visited = [False] * 9

    # 정의된 DFS 함수 호출
    print('======== DFS ========')
    dfs(graph, 1, visited)

    # 각 노드가 방문한 정보를 리스트로 표현
    visited = [False] * 9
    print('\n======== DFS_BFS ========')
    bfs(graph, 1, visited)
