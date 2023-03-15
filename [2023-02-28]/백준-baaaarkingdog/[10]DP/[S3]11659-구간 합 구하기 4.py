import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
d = [0] * (N + 1)

'''
TODO : 다시풀기
1. 각각의 구간합을 1차원 배열로 저장
2. 누적합

'''

total = 0
for i in range(1, N + 1):
    total += nums[i]
    d[i] = total

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    print(d[j + 1] - d[i])
