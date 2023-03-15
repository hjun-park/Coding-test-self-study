import sys

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(10)]


x, y = 1, 1
while True:

    # 시작이야
    if graph[x][y] == 0:
        graph[x][y] = 9

    # 냠냠 먹었어
    elif graph[x][y] == 2:
        graph[x][y] = 9
        break

    # 마지막이야
    if x == 9 and y == 9:
        break

    # 오른쪽으로 못 가고 아래로도 못가
    if graph[x][y + 1] == 1 and graph[x + 1][y] == 1:
        break

    # 가장 먼저 오른쪽을 진행하는데 오른쪽 막혀있으면 아래로 가자
    if graph[x][y + 1] != 1:
        y += 1
    elif graph[x + 1][y] != 1:
        x += 1


for row in graph:
    print(*row)


