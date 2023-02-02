import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = [0] + list(map(int, input().split()))

d = [1] * (N + 2)           # 모든 곳에서 시작하면 결국 count = 1부터 시작하기 때문에 1로 초기화


for i in range(1, N + 1):
    for j in range(1, i + 1):
        if A[j] < A[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
