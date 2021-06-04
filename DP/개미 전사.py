import sys

n = int(input())
k = list(map(int, input().split()))

# 계산된 결과를 저장하기 위한 DP Table
d = [0] * 100

# bottom up 방식 DP
d[0] = k[0]             # 창고가 1개인 경우는 턴 후 식량 d[0]개
d[1] = max(k[0], k[1])  # 창고가 2개인 경우는 둘 중 가장 큰 식량을 보유한 창고가 된다.

# 점화식에 따라서 해당 값이 도출된다.
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

# 계산된 결과
print(d[n - 1])
