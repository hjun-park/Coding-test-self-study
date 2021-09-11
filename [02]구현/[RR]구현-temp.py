import sys

input = sys.stdin.readline

N = int(input())
route = list(map(str, input().split()))
x, y = 1, 1

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D']

for r in route:
    for i in range(len(moves)):
        if r == moves[i]:   # 방향이 같다면 셋팅
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x = nx
    y = ny

print(x, y)


