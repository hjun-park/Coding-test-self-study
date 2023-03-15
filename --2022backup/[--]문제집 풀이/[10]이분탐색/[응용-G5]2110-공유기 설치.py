import sys

input = sys.stdin.readline

N, C = map(int, input().split())
home = sorted([int(input().rstrip()) for _ in range(N)])

'''
    [요약]
    1. 수직선 위에 집 N개 존재, 겹치는 일 없음
    2. 한 집당 공유기 1개, 공유기 거리 최대한 크게 해서 설치하고 싶음
    즉, C개의 공유기를 N개의 집에서 설치해서 가장 인접한 두 공유기 거리를 최대로 하고 싶음
    
    [결과값]
     - 가장 인접한 두 공유기 사이 최대 거리 
         == 여러 공유기 중 최소 거리 값이 모든 케이스에서 가장 커야함
    
    [풀이] https://deok2kim.tistory.com/194 // https://hongcoding.tistory.com/3
    1. 집 정렬
    2. start, end 지정 (집의 최소, 최대 거리로 지정)
    3. mid는 와이파이 간격이며 중앙값으로 지정하고 이분탐색 시작
    4. 처음에는 와이파이를 설치하고 중앙값 마디마다 설치를 해본다.
    5. 와이파이의 개수가 C보다 작으면 더 좁게 설치해야 한다는 의미다.
      -> 따라서 end값을 줄여서 조정한다.
    6. 와이파이의 개수가 C보다 크다면 더 넓게 설치해야 한다는 의미다.
      -> 따라서 start값을 넓혀서 조정한다.
      -> 이 경우 와이파이는 설치 가능하므로 answer값을 mid로 갱신한다. 
'''

result = 0


def binary_search(start, end):
    global result

    while start <= end:
        cnt = 0
        mid_dist = (start + end) // 2

        # 1) 시작점에 와이파이 설치, 카운트 증가
        current_wifi = home[0]
        cnt += 1

        for i in range(1, len(home)):  # 다음 지점부터 와이파이 설치가능 여부 확인
            # 2) 다음 거리에 설치 가능하다면 와이파이 개수 증가
            if current_wifi + mid_dist <= home[i]:
                current_wifi = home[i]  # 현재 와이파이 설치된 위치 갱신
                cnt += 1

        # 3) 설치한 와이파이가 와이파이 개수보다 작다면 더 설치하기 위해 간격을 좁힌다.
        if cnt < C:
            end = mid_dist - 1

        # 4) 설치한 와이파이가 와이파이 개수보다 더 많다면 간격을 넓힌다.
        # 또한, 개수가 많으므로 설치가 가능하므로 와이파이 개수를 갱신한다.
        else:
            start = mid_dist + 1
            result = mid_dist


s = 1
e = home[-1] - home[0]
binary_search(s, e)
print(result)
