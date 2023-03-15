import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())


def calc_dist(home, chicken):
    # min dist 최댓값 초기화
    min_dist = 1e9

    # 치킨집을 순회하면서 계산
    for c in chicken:
        # abs를 이용한 최솟값 계산
        min_dist = min(min_dist, abs(c[0] - home[0]) + abs(c[1] - home[1]))
    # min dist 대입
    return min_dist


# M : 치킨 집 개수
graph = [list(map(int, input().split())) for _ in range(N)]

# 치킨과 집 집계
chicken = [[c, j] for c in range(N) for j in range(N) if graph[c][j] == 2]
home = [[i, j] for i in range(N) for j in range(N) if graph[i][j] == 1]

# 치킨에 대해서 많은 케이스 생성
chicken_select = list(combinations(chicken, M))

# 최소 치킨거리 계산
min_chicken_dist = int(10e9)
for chickens in chicken_select:
    dist = 0
    # 모든 집을 순회하며 치킨 거리 계산
    for h in home:
        dist += calc_dist(h, chickens)
    min_chicken_dist = min(dist, min_chicken_dist)

print(min_chicken_dist)
