import sys
from collections import deque  # 회전 위해

# 톱니바퀴가 1번째나 4번째의 경우 양옆이 존재하지가 않는데 이런 경우는 어떻게 ?
# => 그냥 인자를 그대로 넘겨주고 그 함수에서 해당 num이 0보다 작던지 혹은 3보다 크던지 확인하면 된다.

input = sys.stdin.readline

wheels = []


def left(n, d):
    if n < 0:  # 가장 왼쪽이라면 패스
        return

    # 자기 자신과 그 오른쪽 극이 서로 다르면 회전
    if wheels[n][2] != wheels[n + 1][-2]:
        left(n - 1, -d)  # 왼쪽 회전 체크
        wheels[n].rotate(d)


def right(n, d):
    if n > 3:  # 가장 오른쪽이라면 패스
        return

    # 자기 자신과 그 왼쪽의 극이 서로 다르면 회전
    if wheels[n - 1][2] != wheels[n][-2]:
        right(n + 1, -d)  # 오른쪽 회전 체크
        wheels[n].rotate(d)


# 1) 입력
for _ in range(4):
    wheels.append(deque(list(map(int, input().rstrip()))))

# 2) 회전 입력
for _ in range(int(input().rstrip())):
    num, dir = map(int, input().split())
    num -= 1

    left(num - 1, -dir)
    right(num + 1, -dir)
    wheels[num].rotate(dir)

score = 1
total = 0
for i in range(4):

    if wheels[i][0] == 1:
        total += score

    score *= 2

print(total)
