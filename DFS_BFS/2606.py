from collections import deque


def bfs(graph):
    answer = 0
    visited = {}
    queue = deque([1])  # 1부터 시작

    while queue:
        n = queue.popleft()
        if n not in visited:        # 방문하지 않았다면
            visited.setdefault(n)   # 해당 노드 방문처리
            queue += graph[n]       # 해당 노드와 인접한 행렬들을 모두 큐잉
            answer += 1            # 감염

    # 빠져나왔다면 큐가 비어있는 상태이고 모든 노드를 다 순회했단 얘기
    # return visited, answer    # for debug
    return answer-1


def func():
    # input
    n = int(input())
    pair = int(input())
    # n, pair = map(int, input().splitlines())
    graph = {i: [] for i in range(1, n + 1)}

    # print(graph)

    for i in range(pair):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    # sorting
    for key in graph:
        graph[key].sort()

    # print(graph)      # debug

    # for debug
    # visited, answer = bfs(graph)
    # print(' '.join(list(map(str, visited))))

    answer = bfs(graph)
    print(answer)


if __name__ == '__main__':
    func()
