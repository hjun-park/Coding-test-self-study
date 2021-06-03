import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 범위 확인
        return False

    if graph[x][y] == 0:  # 방문 확인
        graph[x][y] = 1

        # 연결된 상하좌우에 대해서 재귀적으로 호출
        # 연결된 모든 지점에 대해서 방문처리가 끝났다면 True
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True

    else:
        return False


result = 0

for i in range(n):
    for j in range(m):
        # 0, 0부터 탐색 수행
        if dfs(i, j):
            result += 1
print(result)
