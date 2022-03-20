import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chicken = []
result = []  # 구해진 도시 치킨 거리
'''
1) 치킨집을 최대 갯수(M) 설치 해야 거리가 좋다, 즉, M개를 세운 경우에만 루프 진행 (백트래킹)
2) 0, 1, 2 ( 빈칸, 집, 치킨집 )
3) 치킨 거리 : 집에서 가장 가까운 치킨 거리
4) 도시의 치킨 거리 : 모든 치킨 거리를 다 더한 것
5) 최종적으로 구하고자 하는 것 : 가장 적은 치킨거리
'''


# dist 사용하는 것보다 직접 구하는 것이 낫다.
def find_dist(home, chick):
    # print(f'{(r1, c1)} <-> {(r2, c2)} = {int(math.dist([r1, c1], [r2, c2]))}')
    min_dist = int(1e9)

    for c in chick:
        min_dist = min(min_dist, abs(c[0] - home[0]) + abs(c[1] - home[1]))

    return min_dist


# 1) 치킨집 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append([i, j])

# 2) 치킨집 중 M개를 선택 (M개보다 더 작게 고르면 오히려 치킨거리가 길어진다)
for chick in combinations(chicken, M):
    house_min_dist = 0
    city_dist = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:  # 집을 만나면 각 치킨집 별 최소거리 구함
                city_dist += find_dist((i, j), chick)

    # 모든 집을 순회하면 최종 도시 거리가 구해짐, result에 반영
    result.append(city_dist)

print(min(result))
