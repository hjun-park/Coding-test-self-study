import sys

input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]

# 위, 중간, 아래 순으로 길 확인

moves = [(-1, 1), (0, 1), (1, 1)]
result = 0


def dfs(x, y):
    if y == C - 1:
        return True

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and graph[nx][ny] == '.':
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True
    return False


for i in range(R):
    if graph[i][0] == '.':
        if dfs(i, 0):
            result += 1

print(result)
