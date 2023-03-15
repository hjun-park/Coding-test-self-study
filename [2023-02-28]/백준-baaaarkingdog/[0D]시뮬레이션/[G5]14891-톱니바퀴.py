import sys
from collections import deque

input = sys.stdin.readline

wheels = [deque(map(int, input().rstrip())) for _ in range(4)]


def left(n, d):
    if n < 0:  # 톱니바퀴가 왼쪽 범위를 벗어남
        return

    if wheels[n][2] != wheels[n + 1][-2]:  # 기준 바퀴(왼쪽)[2] != 기준 바퀴의 오른쪽[-2]
        left(n - 1, -d)  # 재귀로 가장 맨 왼쪽 먼저 rotate 하도록 수행, 방향은 서로 반대로 돎으로 -d
        wheels[n].rotate(d)


def right(n, d):
    if n > 3:  # 톱니바퀴가 오른쪽 범위를 벗어남
        return

    if wheels[n - 1][2] != wheels[n][-2]:  # 기준 바퀴의 왼쪽[2] != 기준 바퀴(오른쪽)[-2]
        right(n + 1, -d)
        wheels[n].rotate(d)


# 1) 입력
for _ in range(int(input().rstrip())):
    n, d = map(int, input().split())
    n -= 1

    left(n - 1, -d)  # 왼쪽 먼저 재귀적으로 체크
    right(n + 1, -d)
    wheels[n].rotate(d)

score = 0
inc = 1
for wheel in wheels:
    if wheel[0] == 1:
        score += inc

    inc <<= 1

print(score)
