import heapq
import sys

input = sys.stdin.readline

hq = []
for _ in range(int(input().rstrip())):
    x = int(input().rstrip())

    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
