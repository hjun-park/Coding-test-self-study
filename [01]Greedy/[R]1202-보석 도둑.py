import sys
import heapq

input = sys.stdin.readline

'''
    참고: https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-1202-%EB%B3%B4%EC%84%9D-%EB%8F%84%EB%91%91-Python
    핵심:
      1. heapq를 이용한 방법
      2. 파이썬 heapq는 기본으로 min_heap이지만 값을 집어넣을 때 -1을 곱해서 max_heap을 만듦
      3. 보석을 무게별로 heap 에 넣은 후, 가방을 순회하면서 가방 무게보다 적은 보석들의 price를
         모두 또다른 힙에 집어넣음
      4. 가방은 사이즈 순대로 정렬이 된 상태이므로 보석 크기 없이 price만 가지고 넣어도 된다.
'''

N, K = map(int, input().split())
gem = []
for _ in range(N):
    heapq.heappush(gem, list(map(int, input().split())))

bags = []
for _ in range(K):
    bags.append(int(input().rstrip()))
bags.sort()

total = 0
max_gem_price = []    # 특정 가방의 수용 가능한 보석 사이즈들 중 보석의 가치가 제일 비싼 것을 담는 max heap
for bag in bags:
    while gem and bag >= gem[0][0]: # 가방 사이즈에 수용 가능한 보석들은 모두 보석가격 max_heap에 담음
        # 여러 번 push 해도 가방은 작은것부터 큰 순서대로이기 때문에 수용 가능하다.
        heapq.heappush(max_gem_price, -heapq.heappop(gem)[1])

    # 한 번만 담음
    if max_gem_price:
        total -= heapq.heappop(max_gem_price)
    elif not gem:   # 다 비워졌으면
        break
print(total)


