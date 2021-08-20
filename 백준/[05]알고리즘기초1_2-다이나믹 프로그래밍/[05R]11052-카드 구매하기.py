import sys

N = int(input())
p = [0] + list(map(int, sys.stdin.readline().split()))

d = [0] * (N + 1)

# 점화식: d[i] = p[k] + d[i-k]
# d[i] = 카드 i개를 구매하는 최대 가격
# p[k] = k개가 들어있는 카드팩 가격
# i = 구하려는 카드 개수
# k = 카드팩 내 카드 개수

for i in range(1, N+1): # 구매하려는 최대 카드개수 순회
    for k in range(1, i+1):
        d[i] = max(d[i], d[i-k] + p[k])

print(d[N])
