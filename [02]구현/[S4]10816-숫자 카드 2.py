import sys

input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
check = list(map(int, input().split()))

dt = dict()

# 숫자와 그 개수를 딕셔너리에 포함
for i in numbers:
    if i in dt:
        dt[i] += 1
    else:
        dt[i] = 1

for i in check:
    if i in dt:
        print(dt[i], end=' ')  # 있다면 개수를 출력
    else:
        print(0, end=' ')  # 없다면 0을 출력
