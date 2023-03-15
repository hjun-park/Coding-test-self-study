import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
hq = []

for _ in range(N):
    heapq.heappush(hq, int(input().rstrip()))

if len(hq) == 0:
    print(0)

result = 0
while len(hq) > 1:  # 2개를 뽑아서 한꺼번에 처리, 따라서 길이가 1 초과해야 함
    card_pack1, card_pack2 = heapq.heappop(hq), heapq.heappop(hq)

    result += (card_pack1 + card_pack2)
    heapq.heappush(hq, card_pack1 + card_pack2)

print(result)
