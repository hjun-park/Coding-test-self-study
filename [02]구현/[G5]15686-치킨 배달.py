import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

# M : 치킨 집 개수
graph = [list(map(int, input().split())) for _ in range(N)]

# 치킨과 집 집계
chicken = [[c, j] for c in range(N) for j in range(N) if graph[c][j] == 2]
home = [[i, j] for i in range(N) for j in range(N) if graph[i][j] == 1]

# 치킨에 대해서 많은 케이스 생성
chicken_select = combinations(chicken, M)

for i in chicken_select:
    








