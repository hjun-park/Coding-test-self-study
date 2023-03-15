import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
now = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))


def flip_two(x, y):
    temp[x] = 1 - temp[x]
    temp[y] = 1 - temp[y]


def flip_three(x, y, z):
    temp[x] = 1 - temp[x]
    temp[y] = 1 - temp[y]
    temp[z] = 1 - temp[z]


for i in range(2):
    temp = deepcopy(now)
    count = 0

    for j in range(N):
        if j == 0:
            if i == 0 and temp != target:   # i는 0과 1 따라서 처음에 켜고 끄는게 구분되어짐
                flip_two(j, j + 1)
                count += 1

        elif 0 < j < N - 1:
            if temp[j-1] != target[j-1]:    # 하나라도 같은 경우 작동시키지 않음
                flip_three(j - 1, j, j + 1)
                count += 1

        elif j == N - 1:
            if temp[j-1] != target[j-1]:
                flip_two(j - 1, j)
                count += 1

    if temp == target:
        print(count)
        sys.exit(0)

print(-1)
