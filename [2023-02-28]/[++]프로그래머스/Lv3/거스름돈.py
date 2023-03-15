import sys

input = sys.stdin.readline


# 각 동전별로 인해 늘어나는 경우의 수를 적기
# https://hwayomingdlog.tistory.com/100

def solution(n, money):
    # 메모이제이션
    # 각 인덱스에 해당하는 수를 만들 수 있는 가짓수를 기록
    memo = [0] * (n + 1)
    memo[0] = 1
    # 주어진 동전에 하나씩 접근
    for coin in money:
        for price in range(coin, n + 1):
            memo[price] += memo[price - coin]
    answer = memo[n] % 10000000007
    return answer


print(solution(5, [1, 2, 5]))
