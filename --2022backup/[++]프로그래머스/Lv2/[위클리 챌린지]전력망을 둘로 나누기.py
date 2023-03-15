'''
    하나를 끊어서 2개로 분할 시 탑 균등 분배
    [구하는 것] 균등된 2개의 차이 (최대한 작게)

'''

from collections import deque


def bfs(start, visited, graph):
    q = deque()
    q.append(start)
    cnt = 1
    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                q.append(i)
                visited[i] = True

    return cnt


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for a, b in wires:
        visited = [False] * (n + 1)
        visited[b] = True  # 중요: 끊는 대신 방문처리를 해서 방문할 수 없도록 한다.

        # 한쪽은 cnt고 다른 한쪽은 n-cnt 가 된다.
        cnt = bfs(a, visited, graph)

        if abs(cnt - (n - cnt)) < answer:
            answer = abs(cnt - (n - cnt))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
# print(solution(4, [[1, 2], [2, 3], [3, 4]]))
