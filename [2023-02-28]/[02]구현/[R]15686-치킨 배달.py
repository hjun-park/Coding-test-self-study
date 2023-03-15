import sys
from itertools import combinations

# 임의의 두 거리 구하기
# distance =  abs(r1-r2) - abs(c1-c2)

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

'''
 0 - 빈 칸
 1 - 집
 2 - 치킨집
'''


# 0) 치킨 거리 리스트 계산하면서 최솟값을 반환함
def calc_dist(home, chicken):
    # min dist 최댓값 초기화
    min_dist = 1e9

    # 치킨집을 순회하면서 계산
    for c in chicken:
        # abs를 이용한 최솟값 계산
        min_dist = min(min_dist, abs(c[0] - home[0]) + abs(c[1] - home[1]))
    # min dist 대입
    return min_dist


# 1) 치킨 있는 좌표와 집이 있는 좌표 리스트로 입력 받음
chicken = [[c, j] for c in range(n) for j in range(n) if graph[c][j] == 2]
home = [[i, j] for i in range(n) for j in range(n) if graph[i][j] == 1]

# 3) 거리를 담은 리스트 초기화
b = []

# 4) 치킨집을 조합으로 뽑은 리스트를 순회
# 4-1) 집이 있는 좌표를 순회하면서 거리를 계산 ( def calc_dist(home, chicken): )
# 거리를 b리스트에 담기
collect_list = list(combinations(chicken, m))  # 치킨을 m개 뽑는 모든 조합 경우의 수
print(collect_list) # 리스트화 된 조합 예제
print('===========================')

# 5) b 최솟값
for c in collect_list:  # 치킨집 좌표 m개만큼 뽑은 리스트 ([0, 1], [3, 0])
    dist = 0
    for h in home:  # 모든 집을 순회하여 치킨 집 거리 계산
        dist += calc_dist(h, c)
    b.append(dist)


print(min(b))
