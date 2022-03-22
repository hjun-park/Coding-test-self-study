import sys

input = sys.stdin.readline

M, N = map(int, input().split())  # 우주 개수 / 우주에 있는 행성 개수
planets = [list(map(int, input().split())) for _ in range(M)]
sorted_planets = []  # 정렬된 우주 행성
ranks = []  # 랭크

'''
    [요약]
    1. 행성에는 1번부터 N번까지 번호
    2. [구할 것] 균등한 (우주의 쌍)이 몇 개 ?
    3. 구성이 같은데 순서만 다른 우주의 한 쌍은 한 번만 숫자를 센다. (조합)

    [균등 ??]
    1. A 행성의 1보다 2번째 우주가 크거나 작을 때
       B 행성도 1보다 2번째 우주가 크거나 작은 경우
       마찬가지로 같은 경우도 포함한다.


'''

# 정렬본 복사
for planet in planets:
    sorted_planets.append(sorted(planet))

# rank 를 구함
for i in range(M):
    r = []
    for p in sorted_planets[i]:
        r.append(planets[i].index(p))  # index는 가장 먼저 있는 것을 꺼냄
    ranks.append(r)

# 균등한 행성 찾기
cnt = 0

for i in range(M):
    if ranks[i] == 0:  # 이미 방문했던 곳은 건너 뜀
        continue

    find_flag = False
    for j in range(i + 1, M):
        if ranks[i] == ranks[j]:
            ranks[j] = 0
            find_flag = True

    if find_flag:
        cnt += 1  # 한 쌍 찾음

print(cnt)
