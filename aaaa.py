'''

 이때, 가장 다양한 맛을 포함한 케이크 조각은 몇 개의 맛을 포함하고 있는지를 구해서
 return 하도록 solution 함수를 완성해주세요.
'''

import sys
from collections import deque, defaultdict

sys.stdin.readline()

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
_len = 0
graph = []


def bfs(a, b, visited, cut_rows, cut_columns):
    q = deque()
    q.append((a, b))
    my_dict = defaultdict(list)
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < _len and 0 <= ny < _len:
                if not visited[nx][ny]:
                    my_dict['cake'].append(graph[nx][ny])
                    visited[nx][ny] = True
                    q.append((nx, ny))


def solution(cakes, cut_rows, cut_columns):
    global graph
    global _len
    _len = len(cakes[0])
    visited = [[False] * _len for _ in range(_len)]
    for i in range(_len):
        graph.append(list(cakes[i]))

    answer = 0
    print(_len)
    # print(graph)
    return _len
