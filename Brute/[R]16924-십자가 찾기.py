import sys

input = sys.stdin.readline

N, M = map(int, input().split())

'''
 참고: https://hjp845.tistory.com/153 
'''

graph = [input().rstrip() for _ in range(N)]
check = [[0] * M for _ in range(N)]
info = []

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def find_cross(x, y):
    for s in range(1, M):
        flag = True
        for d in range(4):  # 4방향으로 해서 십자가 사이즈 1부터 M까지 찾아감
            nx = x + dx[d] * s
            ny = y + dy[d] * s

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '*':
                pass
            else:
                flag = False
                break

        if flag:  # 적당한 십자가 사이즈 s를 찾은 경우
            info.append([x + 1, y + 1, s])
            for d in range(4):
                nx = x + dx[d] * s
                ny = x + dy[d] * s
                check[nx][ny] = 0
            check[x][y] = 0
        else:
            break


for i in range(N):
    for j in range(M):
        if graph[i][j] == '*':
            check[i][j] = 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == '*':
            find_cross(i, j)

total = 0
for i in range(N):
    for j in range(M):
        total += check[i][j]

if total == 0:
    print(len(info))
    for i in info:
        print(*i)
else:
    print(-1)
