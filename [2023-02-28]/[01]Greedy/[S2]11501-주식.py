import sys

input = sys.stdin.readline

T = int(input().rstrip())

# 핵심
# 뒤에서부터 접근하며, max_price보다 탐색하는 인덱스 가격이 더 작은 경우라면 그 차익을 더해준다.
'''
    예시)
    10 7 5 9 가 있을 때 9에서부터 탐색 시작
    1. max_price는 9이고, 9와 5비교 시 9가(뒤) 더 크기 때문에 차익을 챙긴다 ( 9 - 5 = 4 )
    2. max_price와 7비교 시 9가(뒤) 더 크기 때문에 차익을 챙긴다. ( 9 - 7 = 2 )
    3. max_price인 9와 10 비교 시 10이 더 크기 때문에 max_price를 10으로 갱신한다.
    4. 이익은 6
'''

for _ in range(T):
    N = int(input().rstrip())  # day
    prices = list(map(int, input().split()))
    value = 0
    max_price = 0

    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > max_price:  # 현재가가 더 큰 경우라면 (사야할 때)
            max_price = prices[i]  # 갱신
        else:
            value += max_price - prices[i]  # 팔아야할 때

    print(value)
