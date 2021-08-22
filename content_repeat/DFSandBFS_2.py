import sys
from collections import deque


def dfs(graph, v, visited):
    # 1. 방문처리
    visited[v] = True

    # 2. dfs는 방문처리 한 것은 출력
    print(v, end=' ')

    # 3. 방문지와 인접한 모든 노드 확인
    for i in graph[v]:
        # 4. 만약 인접노드를 방문하지 않았다면
        if not visited[i]:
            # 5. 재귀를 이용해 끝까지 확인
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    ## 빌드업 과정
    # 1. 방문처리
    visited[start] = True
    # 2. 큐 생성 및 최초 시작지 append
    queue = deque([start])

    # 3. 큐 내용 순회
    while queue:
        # 4. 처음 노드 값 추출 후 바로 출력
        v = queue.popleft()
        print(v, end=' ')

        # 5. 출력노드와 인접한 리스트 방문 확인
        for i in graph[v]:
            # 6. 만약 인접한 노드 중 방문하지 않은 곳이 있다면
            if not visited[i]:
                # 7. 큐에 집어넣기
                queue.append(i)
                # 8. 집어넣은건 꺼내고 바로 출력처리 될 것이므로 미리 방문처리
                visited[i] = True

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
