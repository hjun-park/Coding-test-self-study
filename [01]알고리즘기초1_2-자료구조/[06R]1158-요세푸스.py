import sys

N, K = map(int, sys.stdin.readline().split())

queue = [x + 1 for x in range(N)]

answer = []
index = 0

for _ in range(N):
    index += K - 1
    # index %= N
    if index >= len(queue):
        index = index % len(queue)

    answer.append(str(queue.pop(index)))
print("<", ", ".join(answer)[:], ">", sep='')
