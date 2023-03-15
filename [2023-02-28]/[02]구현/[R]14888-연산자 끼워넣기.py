import sys

'''
 백트래킹 ( DFS )
 - https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python 
'''
input = sys.stdin.readline

N = int(input())  # Number 개수
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))

result = [1e9, -1e9]


def dfs(total, depth, plus, minus, mul, div):
    global result
    if depth == N:
        result[0] = min(total, result[0])
        result[1] = max(total, result[1])

    if plus:
        dfs(total + numbers[depth], depth + 1, plus - 1, minus, mul, div)
    if minus:
        dfs(total - numbers[depth], depth + 1, plus, minus - 1, mul, div)
    if mul:
        dfs(total * numbers[depth], depth + 1, plus, minus, mul - 1, div)
    if div:
        dfs(int(total / numbers[depth]), depth + 1, plus, minus, mul, div - 1)


dfs(numbers[0], 1, ops[0], ops[1], ops[2], ops[3])
print(result[1])
print(result[0])
