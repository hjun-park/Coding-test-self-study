import sys

input = sys.stdin.readline

N = int(input().rstrip())
stairs = [0] + [int(input().rstrip()) for _ in range(N)]
d = [0] * 10_002

'''
(1) dp 테이블 정의
 - d[i] = N
 - i층까지 올라갔을 때 얻을 수 있는 최대 점수 N
 
(2) 초깃값 선정
 - d[1] = d[1]
 - d[2] = d[1] + d[2]
 
(3) 점화식 작성
  - 1개 => d[1]
  - 2개 => d[1] + d[2]
  - 3개 => max(d[1] + d[3],   d[2] + d[3])
  - 4개 => max(d[1] + d[2] + d[4],  d[1] + d[3] + d[4])
  즉, 이전 계단을 밟지 않고 d-2 dp를 불러 오는지,
      이전 계단을 밟고(f) f-2 dp를 불러온 것 중 큰 값
      
계단은 자연수만 적혀 있기 때문에 다른 경우는 고민할 필요 없음

'''


def logic():
    global d, stairs

    if N == 1:
        d[1] = stairs[1]
        return
    elif N == 2:
        d[2] = stairs[1] + stairs[2]
        return

    d[1] = stairs[1]
    d[2] = stairs[1] + stairs[2]
    for n in range(3, N + 1):
        d[n] = max(stairs[n] + d[n - 2],
                   stairs[n] + stairs[n - 1] + d[n - 3])


logic()
print(d[N])
