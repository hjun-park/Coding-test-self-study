import sys
from collections import defaultdict

input = sys.stdin.readline

M, N = map(int, input().split())  # 우주 개수 / 우주에 있는 행성 개수

'''
    이분탐색이 아닌데 ?????
    
    [요약]
    1. 행성에는 1번부터 N번까지 번호
    2. [구할 것] 균등한 (우주의 쌍)이 몇 개 ?
    3. 구성이 같은데 순서만 다른 우주의 한 쌍은 한 번만 숫자를 센다. (조합)

    [균등 ??]
    1. A 행성의 1보다 2번째 우주가 크거나 작을 때
       B 행성도 1보다 2번째 우주가 크거나 작은 경우
       마찬가지로 같은 경우도 포함한다.


    [풀이과정]
    0. defaultdict 생성 (균등한 생성을 카운트 하기 위함) -> universe
    1. 행성 입력받음 -> planets
    2. 입력받은 행성을 정렬하고 압축함 -> sorted_planets
    3. 압축한 행성으로 랭크 리스트 사전을 생성 -> ranks
    4. 행성을 순회하며 랭크로 새로운 배열 생성 -> rank_planets
    5. universe 딕셔너리에 rank_plantes의 cnt를 +1 증가 ( 균등한 생성 카운트 )
    6. 균등한 쌍 갯수 출력
'''

# 0) 균등한 행성을 카운트하기 위함
universe = defaultdict(int)
for i in range(M):
    # 1) 행성 입력 [12, 50, 50, 11]
    planets = list(map(int, input().split()))

    # 2) 정렬 and 압축된 행성 [11, 12, 50]
    sorted_planets = sorted(list(set(planets)))

    # 3) 압축된 행성 기준으로 ranks 딕셔너리 생성 {11:0, 12:1, 50:2}
    ranks = {sorted_planets[x]: x for x in range(len(sorted_planets))}

    # 4) planets을 순회하며 ranks로 변환한 리스트 생성 (1, 2, 2, 0)
    # 참고로 defaultdict에 집어넣을 때에는 list가 아닌 tuple을 집어넣어야 한다.
    # 한 마디로, 딕셔너리 사용할 때에는 튜플을 사용하자
    rank_planets = tuple([ranks[x] for x in planets])

    # 5) 생성된 rank_planets를 universe 에 +1하기 (균등한 행성을 만나면 개수가 늘어남)
    universe[rank_planets] += 1

# 6) 균등한 쌍의 개수를 출력
cnt = 0
for v in universe.values():
    cnt += v * (v - 1) // 2  # 0~N 까지의 합을 구하는 예제

print(cnt)
