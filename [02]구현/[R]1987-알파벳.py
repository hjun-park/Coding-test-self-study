import sys

input = sys.stdin.readline

# 세로, 가로
# (0, 0)
# 백트래킹
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
alpha_list = []
max_count = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 1) 알파벳의 중복을 체크하는 방법
# 2) 말이 지나가는 방법 (백트래킹)


def dfs(x, y, count):
    global max_count
    alpha_list.append(graph[x][y])
    # print(alpha_list)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and graph[nx][ny] not in alpha_list:
                visited[nx][ny] = True
                dfs(nx, ny, count + 1)
                alpha_list.pop()
                visited[nx][ny] = False

    # print(count)
    max_count = max(count, max_count)


visited[0][0] = True
dfs(0, 0, 1)

# for i in range(R):
#     for j in range(C):
#         count = 1
#         visited[i][j] = True
#         dfs(i, j, count)
#         visited[i][j] = False

print(max_count)
