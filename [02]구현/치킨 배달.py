import sys
from itertools import combinations

'''
    1. 문제에서 요구하는 치킨 집 개수는 m <= 치킨집 개수 <= 13 이다.
    2. 순열조합 문제로 생각해 보았을 때 13개 중 m개를 택하는 경우로써 13Cm 이다. => 연산이 그리 많지 않다. => 전수조사 방법 가능
    3. Combinations 라이브러리를 이용하여 순열조합 가능
'''

n, m = map(int, sys.stdin.readline().split())  # 줄 라인 / 남기려는 치킨집 개수
chicken, house = [], []

# 2차 행렬을 한번에 입력받을 필요 없이 라인 수만큼 입력받음
# 치킨과 집은 좌표를 튜플 형식(x, y)으로 리스트에 저장
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))  # 총 리스트 chicken 개수 중에서 m개만을 선택하는 경우
print(f'candidate: {candidates}')


# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0

    # 모든 집에 대하여 가까운 치킨집 찾기
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:    # 치킨집 거리
            temp = min(temp, abs(hx - cx) + abs(hy - cy))   # 집거리 - 치킨집 거리 해서 최소 치킨거리를 구함

        # 가장 가까운 치킨집 거리 더하기
        result += temp

    # 치킨 거리 합 반환
    return result


# 치킨 거리의 최소값 출력
result = 1e9
for candidate in candidates:  # 여러 조합 중 하나씩 최소 치킨 거리 구해서 result에 저장
    result = min(result, get_sum(candidate))

print(result)
