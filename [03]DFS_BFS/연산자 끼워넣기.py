import sys
from itertools import product

# 사칙연산을 사용하기 때문에 중복순열을 사용 => product 라이브러리 사용
# 아래와 같이 해결할 수 있지만 아래 코드에서는 중복 순열을 사용하지 않고 DFS를 사용
'''
n = 4
print(list(product(['+', '-', '*', '/'], repeat=(n - 1))))
'''

n = int(input())  # 수의 개수
data = list(map(int, input().split()))  # 연산 수행하고자 하는 리스트
add, sub, mul, div = map(int, input().split())  # 더하기 / 빼기 / 곱하기 / 나누기 연산 개수

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9


# DFS 메소드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    # 아닌 경우 각 연산자에 대해 재귀적으로 수행
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1


dfs(1, data[0])

# 최댓값과 최솟값 출력
print(max_value)
print(min_value)
