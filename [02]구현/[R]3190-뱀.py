import sys

n = int(input())    # 보드의 크기
k = int(input())    # 사과 개수
graph = []
apples = []
moves = []

for _ in range(k):
    x, y = map(int, input().split())    # 사과 좌표
    apples.append((x, y))
    graph[x][y] = 1 # 사과 좌표 찍기

l = int(input())    # 뱀의 방향 전환 정보
for _ in range(l):
    sec, dir = map(str, input().split())
    sec = int(sec)
    moves.append((sec, dir))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작 위치



