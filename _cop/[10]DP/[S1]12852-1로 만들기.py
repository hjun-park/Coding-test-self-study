import sys

input = sys.stdin.readline

N = int(input().rstrip())

d = [0] * (N + 2)
pre = [0] * (N + 2)  # 이전 수 추적용


def logic():
    for i in range(2, N + 1):
        d[i] = d[i - 1] + 1
        pre[i] = i - 1

        if i % 3 == 0 and d[i // 3] + 1 < d[i]:
            d[i] = d[i // 3] + 1
            pre[i] = i // 3

        if i % 2 == 0 and d[i // 2] + 1 < d[i]:
            d[i] = d[i // 2] + 1
            pre[i] = i // 2


logic()
print(d[N])
cur = N
while True:
    print(cur, end=' ')
    if cur == 1:
        break

    cur = pre[cur]
