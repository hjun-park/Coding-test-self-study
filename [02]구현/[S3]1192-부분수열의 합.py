import sys

input = sys.stdin.readline

'''
 https://esoongan.tistory.com/79
 1) DFS를 이용한 재귀 풀이
 2) itertools를 이용한 완전탐색
'''

N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0


def dfs(idx, sum):
    global count

    if idx >= N:  # 숫자 인덱스 범위 초과
        return

    sum += nums[idx]
    if sum == S:
        count += 1
    dfs(idx + 1, sum)
    dfs(idx + 1, sum - nums[idx])


dfs(0, 0)
print(count)
