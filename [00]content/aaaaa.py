import sys

input = sys.stdin.readline

# while True:
#     num = input().rstrip()
#
#     if num == '0':
#         break
#     else:
#         num_list = list(map(int, num))


print((lambda x: x * (x + 1) // 2)(int(input().rstrip())))

