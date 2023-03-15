import sys

input = sys.stdin.readline

# DP 문제

N = int(input().rstrip())
nums = list(map(int, input().split()))
d = [1] * (N + 2)  # 편의를 위해 1부터 초기화, +2는 넉넉하게 준 것

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:  # 큰 경우에만 부분 수열로 넣을 수 있음 = 카운트 셈
            d[i] = max(d[i], d[j] + 1)  # 인덱스 잡은 자리와 현재 자리를 비교해서 가장 큰 count 값을 집어넣음

print(max(d))  # 가장 큰 것이 가장 긴 증가하는 부분 수열의 최대 element 개수
