import sys

input = sys.stdin.readline

N = int(input().rstrip())
serial = []

for _ in range(N):
    serial.append(input().rstrip())


def sum_num(arr):
    result = 0
    for num in arr:
        if num.isdigit():
            result += int(num)
    return result

# 함수를 이용해서 정렬도 가능하다.
serial.sort(key=lambda x: (len(x), sum_num(x), x))

for s in serial:
    print(s)
