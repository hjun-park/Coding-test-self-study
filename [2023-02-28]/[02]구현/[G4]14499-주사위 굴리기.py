import sys

input = sys.stdin.readline

# 오, 왼, 상, 하
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0] * 6

for i in range(k):
    dir = order[i]

    nx = x + dx[dir]
    ny = y + dy[dir]

    # 주사위 굴린 것이 범위를 벗어날 때
    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    # 아래와 위는 5, 0으로 고정하고 동서남북 굴렸을 때 각각 어떻게 표기되는지를 적는다.
    if dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    # 좌표가 0인 경우 주사위 좌표를 대입
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:   # 좌표에 값이 있는 경우 주사위에 대입 후 좌표는 0으로 초기화
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0

    # 이동
    x, y = nx, ny

    # 출력은 주사위의 맨 윗면
    print(dice[0])

