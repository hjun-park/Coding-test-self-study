import heapq
import sys

input = sys.stdin.readline

'''
    출처: https://skgudwn34.tistory.com/26
'''

n = int(input())
univ = []
for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    univ.append((d, p))

univ.sort()

min_pay_list = []

for u in univ:  # u(일정, 가격)
    heapq.heappush(min_pay_list, u[1])  # 가격넣기 ( heapq에서 적은순서로 정렬 )

    # 가격을 적게 주는 대학교 리스트(가격, 날짜)를 하나씩 제거합니다.
    # 즉, 날짜가 1, 2, 3 증가할 때마다 가장 높은 가격을 주는 학교만 하나씩 남겨놓는 원리
    # ex) u[0]이 1이면 1일차만 들어갈 수 있다. 즉 가장 돈 잘 주는 1개만 남겨놓아야 하므로
    # 2개 이상값이 min_pay_list에 들어가면 리스트를 하나 빼준다.
    if len(min_pay_list) > u[0]:
        heapq.heappop(min_pay_list)  # 하나 남을 때까지 뺀다.

print(sum(min_pay_list))
