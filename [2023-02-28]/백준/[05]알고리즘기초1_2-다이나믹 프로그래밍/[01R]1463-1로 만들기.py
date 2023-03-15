import sys

N = int(input())
count = 0

d = [0] * (N + 1)

# 점화식
# d[n] = min(d[n//3], d[n//2], d[n-1]) + 1

for i in range(2, N + 1):
    # 먼저 1을 빼는 경우 나오는 수 저장
    d[i] = d[i - 1] + 1

    # 2를 나누는 경우가 더 최솟값이 나온다면
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1

    # 3을 나누는 경우가 더 최솟값이 나온다면
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1


print(d[N])
