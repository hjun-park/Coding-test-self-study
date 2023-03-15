import sys

input = sys.stdin.readline

N = int(input().rstrip())

'''
    참고: https://kyun2da.github.io/2021/04/06/dragonCurve/
    
    규칙: 이전 세대의 정보를 뒤집어서 거기에 1을 더해주고 뒤에 추가한다.
    코드: (move[-i -1 ] + 1 % 4) 라는 규칙이 만들어진다. g 세대만큼 반복
    즉, 0세대 : 0 
        1세대 : 0 // 1
        2세대 : 0 1 // 2 1
        3세대 : 0 1 2 1 // 2 3 2 1
        4세대 : 0 1 2 1 2 3 2 1 // 2 3 4 3 2 3 2 1
'''

graph = [[0] * 101 for _ in range(101)]

# 동, 북, 서, 남 (문제에서는 x, y 좌표가 서로 반대된 상태)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1  # 시작점은 1로 셋팅

    # 처음 진행방향을 저장
    move = [d]
    # 세대만큼 반복해서 드래곤 커브를 생성함
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)

    # 이동을 하면서 드래곤 커브를 지정함
    for d in move:
        nx = x + dx[d]
        ny = y + dy[d]
        graph[nx][ny] = 1
        x, y = nx, ny

# 모든 꼭짓점이 드래곤 커브인 정사각형 개수 구하기
answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            answer += 1

print(answer)
