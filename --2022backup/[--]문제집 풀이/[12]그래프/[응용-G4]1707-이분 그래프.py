import sys
from collections import deque

input = sys.stdin.readline

K = int(input().rstrip())


def bfs(start, color):
    global colors, is_bipartite
    q = deque()
    q.append(start)
    colors[start] = color

    while q and is_bipartite:
        v = q.popleft()

        for e in graph[v]:
            # 색이 칠해지지 않은 ( 미방문 ) 지역의 경우 반대의 색을 칠해준 후 큐에 집어넣기
            if colors[e] == 0:
                colors[e] = colors[v] * (-1)
                q.append(e)

            # 색이 칠해져 있는 경우 접점의 색을 체크 (더해서 0이 아니라면 같은 색으로 칠해져 있단 의미
            # 즉, 인접한 영역이 같은 색으로 칠해져 있다면 이는 이분 그래프가 아니다.
            if colors[v] + colors[e] != 0:
                is_bipartite = False
                return


for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    is_bipartite = True

    # 1) 컬러 기록할 리스트
    colors = [0 for _ in range(V + 1)]

    # 2) 그래프 형성
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 3) color가 칠해지지 않았다면 (0) bfs 순회 (for을 돌리는 이유는 전부 연결된 그래프가 아닌 경우도 있어서다.)
    for i in range(1, V + 1):
        if not is_bipartite:  # 이진그래프가 아니라면 바로 끝
            break

        if colors[i] == 0:
            bfs(i, 1)

    print('YES' if is_bipartite else 'NO')

'''
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

YES
NO
'''
