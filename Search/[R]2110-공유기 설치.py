import sys

input = sys.stdin.readline

'''
    이해 가는 예제: https://my-coding-notes.tistory.com/119
                  https://bgeun2.tistory.com/63
    
'''

def binary_search(target, start, end):
    global result
    while start <= end:
        count = 1  # 공유기 개수 (처음에는 설치하고 시작)
        current = house[0]  # 공유기가 설치된 집의 위치
        mid = (start + end) // 2

        for i in range(1, len(house)):
            if house[i] >= current + mid:   # 만약 집 위치가 중간거리값 이상이라면
                count += 1                  # 공유기를 설치한다.
                current = house[i]          # 다음 공유기가 설치된 곳으로 위치 변경

        if count >= target: # mid값에 따라 설치된 공유기의 개수가 target보다 많거나 같으면
            start = mid + 1
            result = mid
        else:   # target 보다 공유기 개수가 적다면 거리를 줄인다.
            end = mid - 1

    print(result)


N, C = map(int, input().split())
house = []

for _ in range(N):
    house.append(int(input()))

house.sort()

# 좌표값의 최소값
start = 1
end = house[-1] - house[0]

result = 0

binary_search(C, start, end)
