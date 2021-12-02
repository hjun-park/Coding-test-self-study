import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
hq = []

for _ in range(N):
    heapq.heappush(hq, int(input().rstrip()))

'''
    문제 핵심
    1) 순차적으로 작은 것부터 하나하나 뽑아서 더하는 것이 솔루션
    2) 두 수를 더하면 그게 새로운 카드이며, 카드리스트에 그것보다 작은 값이 있다면 
       두 수를 더해 나온 카드는 나중에 뽑아도 된다.
    3) 길이가 1인 경우는 비교할 이유가 없다. (0번)
'''

if len(hq) == 0:
    print(0)

result = 0
while len(hq) > 1:  # 한 번에 2개를 뽑을 것이기 때문에 길이가 2 이상
    pack1 = heapq.heappop(hq)
    pack2 = heapq.heappop(hq)

    result += (pack1 + pack2)
    heapq.heappush(hq, pack1 + pack2)

print(result)
