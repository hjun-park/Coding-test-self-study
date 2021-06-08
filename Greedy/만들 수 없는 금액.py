import sys

n = int(input())
coins = list(map(int, sys.stdin.readline().split(' ')))
coins.sort()

target = 1
for coin in coins:
    # 만들 수 없는 금액을 찾았을 때 종료
    if target < coin:
        break
    target += coin

# 만들 수 없는 금액 출력
print(target)






