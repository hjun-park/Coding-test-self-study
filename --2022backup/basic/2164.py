# queue 문제
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

num_queue = deque([x for x in range(1, N + 1)])

while not (len(num_queue) == 1):
    num_queue.popleft()
    temp = num_queue.popleft()
    num_queue.append(temp)

print(num_queue[0])
