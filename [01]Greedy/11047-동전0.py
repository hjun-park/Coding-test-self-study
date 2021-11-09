import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(N)]

count = 0
for coin in reversed(coins):  # 정렬 상태서 시작
    if coin > K:  # 나눌 수 없는 경우
        continue

    elif K == 0:  # 다 나누어졌다면
        break

    count += (K // coin)
    K %= coin

print(count)
