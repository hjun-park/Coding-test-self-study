import sys
from collections import deque  # rotate 사용 위함

input = sys.stdin.readline

wheels = []
for _ in range(4):
    wheels.append(deque(list(map(int, input().rstrip()))))

# 회전 횟수
K = int(input().rstrip())
R = [list(map(int, input().split())) for _ in range(K)]


def left(num, d):
    if num < 0:
        return
    if wheels[num][2] != wheels[num + 1][-2]:
        left(num - 1, -d)
        wheels[num].rotate(d)


def right(num, d):
    if num > 3:
        return
    if wheels[num][-2] != wheels[num - 1][2]:
        right(num + 1, -d)
        wheels[num].rotate(d)


for i in range(K):
    num = R[i][0] - 1
    direction = R[i][1]

    left(num - 1, -direction)
    right(num + 1, -direction)
    wheels[num].rotate(direction)

answer = 0
for i in range(4):
    answer += (2**i) * wheels[i][0]

print(answer)
