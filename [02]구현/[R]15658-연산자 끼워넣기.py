import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9    # 입력값 조심 


def dfs(total, depth, plus, minus, mul, div):
    global min_value, max_value

    if depth == N:
        min_value = min(total, min_value)
        max_value = max(total, max_value)
        return

    if plus:
        dfs(total + nums[depth], depth + 1, plus - 1, minus, mul, div)
    if minus:
        dfs(total - nums[depth], depth + 1, plus, minus - 1, mul, div)
    if mul:
        dfs(total * nums[depth], depth + 1, plus, minus, mul - 1, div)
    if div:
        dfs(int(total / nums[depth]), depth + 1, plus, minus, mul, div - 1)


dfs(nums[0], 1, ops[0], ops[1], ops[2], ops[3])
# dfs(0, 0, ops[0], ops[1], ops[2], ops[3])
print(max_value)
print(min_value)
