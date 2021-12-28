import sys

input = sys.stdin.readline

graph = [list(map(int, input().rstrip())) for _ in range(9)]


def valid(x, y, num):
    # 가로 탐색
    for col in range(9):
        if graph[x][col] == num:
            return False

    # 세로 탐색
    for row in range(9):
        if graph[row][y] == num:
            return False

    # 3x3 탐색
    start_row = x // 3 * 3
    start_col = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if graph[start_row + i][start_col + j] == num:
                return False

    # 모든 탐색을 마치면 True
    return True


def find_empty():
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                return i, j
    return None, None


# 백트래킹을 이용하여 계산해야 한다.
def dfs():
    # 1) 스도쿠에 빈 공간이 있는지 확인한다. 없으면 종료한다.
    r, c = find_empty()

    # DFS의 종료조건: r이 True라면
    if r is None:
        return True

    # 2) 빈 공간이 있다면 어떤 값이 들어갈 수 있는지 탐색 (가로, 세로, 3x3)
    #  - 찾으면 스도쿠에 집어넣는다.
    #  - 채워넣을 수 있는게 없다면 백트래킹
    else:
        for i in range(1, 10):
            if valid(r, c, i):  # 유효하면 값 집어넣기
                graph[r][c] = i
                if dfs():  # 추가한 값에 대해 다시 DFS를 수행한다.
                    return True
                graph[r][c] = 0  # 백트래킹
        return False


dfs()
for i in range(9):
    for j in range(9):
        print(graph[i][j], end='')
    print()
