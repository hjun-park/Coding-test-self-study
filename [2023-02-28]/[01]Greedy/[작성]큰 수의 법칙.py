import sys

# n, m, k = map(int, input().split())
# numbers = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
#
# result = 0
# i = 0
# # for num in numbers:
# while m > i:
#     for j in range(k):
#         result += numbers[0]
#         i += 1
#
#     result += numbers[1]
#     i += 1
#
# print(result)

n, m, k = map(int, input().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

first_num = numbers[0]
second_num = numbers[1]

count = (m // (k + 1)) * k
count += (m % (k + 1))

result = 0
result += count * first_num
result += (m-count) * second_num

print(result)
