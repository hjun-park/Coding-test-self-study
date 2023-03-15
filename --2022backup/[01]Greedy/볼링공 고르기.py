import sys

n, m = map(int, input().split(' '))
data = list(map(int, input().split()))

# ===================================
# 비효율적 방식
# ===================================
# result = 0
# for num1, i in enumerate(data):
#     for num2, j in enumerate(data):
#         if num1 == num2 or i == j:
#             continue
#         else:
#             result += 1
#
# print(result//2)

# 효율적

# ===================================
# 효율적 방식
# ===================================
# 볼링공의 무게 ( 1kg ~ 10kg )담을 리스트
array = [0] * 11

for x in data:
    # 각 무게 해당하는 볼링 수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수)는 제외 = B가 선택하는 경우의 수
    result += array[i] * n  # A가 선택할 수 있는 개수 * B가 선택할 수 있는 개수

print(result)
