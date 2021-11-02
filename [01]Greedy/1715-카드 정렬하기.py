import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = []

for _ in range(N):
    heapq.heappush(numbers, int(input().rstrip()))

'''
    문제 핵심
    1) 순차적으로 작은 것부터 하나하나 뽑아서 더하는 것이 솔루션
    2) 두 수를 더하면 그게 새로운 카드이며, 카드리스트에 그것보다 작은 값이 있다면 
       두 수를 더해 나온 카드는 나중에 뽑아도 된다.
    3) 길이가 1인 경우는 비교할 이유가 없다. (0번)
'''

if len(numbers) == 0:
    print(0)

result = 0
while len(numbers) > 1:
    card1 = heapq.heappop(numbers)
    card2 = heapq.heappop(numbers)
    result += (card1 + card2)
    heapq.heappush(numbers, card1 + card2)

print(result)
