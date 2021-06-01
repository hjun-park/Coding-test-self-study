import sys

N, M, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()

first = num_list[-1]
second = num_list[-2]

### 1차 풀이
# result = 0
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         result += first
#         M -= 1
#     if M == 0:
#         break
#     result += second
#     M -= 1
#
# print(result)


### 수열을 이용한 개선된 풀이
count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += count * first  # 가장 큰 수 더하기
result += (M - count) * second  # 다음으로 큰 수 더하기

print(result)
