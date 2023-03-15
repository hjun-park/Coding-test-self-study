'''
    https://ebbnflow.tistory.com/173  => 해당 블로그가 자세한 설명
    sudocode :
        create a queue Q
        mark v as visited and put v into Q
        while Q is non-empty
        remove the head u of Q
        mark and enqueue all (unvisited) neighbours of u
'''

'''
    BFS 로직
        Q라는 큐 생성 -> V 방문 했다고 치고 Q에 저장 
        -> Q가 빌 때까지 계속 while 루프 돌면서
        -> 가장 먼저 Q의 머리 부분을 꺼냄 이를 u라고 함 (moveleft)
        -> u와 인접한 위치에 있는 방문하지 않은 노드들을 마킹하고 enqueue 함
'''

'''
    DFS 로직 [ 재귀 : 실행 초기화, 반복 부분 따로 만들기 ]
        1) 스택에 시작 노드를 넣는다.
        2) 스택이 비어있으면 실행을 멈추고 False 반환.
        3) 스택의 맨 위 노드가 찾고자 하는 노드라면 탐색을 종료하고 True 반환.
        4) 3.번에서 스택의 맨 위 노드가 찾고자하는(방문하지 않은) 노드가 아니라면 해당 노드를 Pop하고, 
           스택에 들어온 적 없는 Pop한 노드의 모든 이웃 노드를 찾아 순서대로 스택에 Push
        5) 3.으로 돌아간다.
'''

'''
    인접행렬보다 인접리스트로 구하는 것이 속도 면에서 더욱 좋다.
'''
import sys

input = sys.stdin.readline
from collections import deque


def dfs(graph, v):
    visited = {}
    stack = [v]                           # 시작지점 스택에 넣고 시작

    while stack:                          # 스택 값 빌 때까지 돌기
        n = stack.pop()                   # 스택 내용 빼고
        if n not in visited:              # 방문처리가 되지 않았다면
            visited.setdefault(n)         # 방문처리 ( 딕셔너리라서 중복된 값이 들어가면 무시된다 )
            stack += reversed(graph[n])   # 해당 노드에 있는 간선 모두 저장 ( 스택은 LIFO이기 때문에 거꾸로 집어넣음 )
    return visited                        # stack이 빈다면 반환


def bfs(graph, v):
    visited = {}
    queue = deque([v])

    while queue:
        n = queue.popleft()                  # 큐에서 빼고
        if n not in visited:                 # 방문을 안 한 노드라면
            visited.setdefault(n)            # 방문처리 ( 딕셔너리라서 중복된 값이 들어가면 무시된다 )
            queue += graph[n]                #
    return visited


if __name__ == '__main__':
    # n : 노드 개수
    # m : 간선 개수
    # v : 시작 번호
    n, m, v = map(int, input().split())

    graph = {i: [] for i in range(1, n + 1)}    # 노드 개수 만큼 리스트 포함하는 딕셔너리 생성

    # 간선 개수만큼 (5번) 순환하면서 입력받은 시작, 도착지 값을 서로의 그래프 값으로 저장
    for i in range(1, m + 1):
        x, y = map(int, input().split())
        graph[x].append(y)  # 그래프 딕셔너리의 x번째 리스트에 y라는 값을 추가
        graph[y].append(x)

    # graph 딕셔너리 내의 키값을 모두 정렬하면 인접리스트가 생성됨
    for key in graph:
        graph[key].sort()

    print('============')
    print(graph)

    print(' '.join(list(map(str, dfs(graph, v)))))
    print(' '.join(list(map(str, bfs(graph, v)))))
