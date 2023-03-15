# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
#
# def lcm(x, y):
#     return (x * y) // gcd(x, y)
#
#
# def solution(arr):
#     temp = arr[0]
#     for i in range(1, len(arr)):
#         temp = lcm(temp, arr[i])
#
#     return temp
#
# arr = list(map(int, input().split()))
#
# print(solution(arr))


N = int(input())
count_list = list(map(int, input().split()))
d = [0] * 23

for i in count_list:
    d[i-1] += 1

print(' '.join(map(str, d)))


