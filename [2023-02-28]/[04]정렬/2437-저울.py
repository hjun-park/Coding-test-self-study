import sys

input = sys.stdin.readline

N = int(input().rstrip())
weights = list(map(int, input().split()))

# 저울의 무게 합까지는 모두 구할 수 있음
weights.sort()

num = 1  # 측정예정최솟값
for i in range(N):
    if num < weights[i]:  # 추의 무게보다 예정최솟값이 더 작은 경우 (측정불가)
        break
    else:
        num += weights[i]

print(num)
