# # import sys
# # from collections import deque
# #
# # input = sys.stdin.readline
# #
# # N = int(input().rstrip())
# #
# # s = deque()
# # remains = []
# # max_diff = -1
# #
# # if s == sorted(s, reverse=True):
# #     print(-1)
# #     sys.exit(0)
# #
# #
# # for _ in range(N):
# #     s.append(int(input().rstrip()))
# #
# # while s:
# #     num = s.popleft()
# #
# #     for r in remains:
# #         if num > r:
# #             max_diff = max(max_diff, num - r)
# #
# #     remains.append(num)
# #
# # print(max_diff)
#
# # import sys
# # from collections import deque
# #
# # input = sys.stdin.readline
# #
# # s = list(map(int, input().rstrip()))
#
# import sys
#
# input = sys.stdin.readline
#
# # N = int(input().rstrip())
# # numbers = []
# # for _ in range(N):
# #     numbers.append(int(input().rstrip()))
# # th = int(input().rstrip())
#
# N = 6
# numbers = [1, 3, 4, 5, 2, 6]
# th = 4
# #
# # N = 3
# # numbers = [1, 5, 2]
# # th = 2
#
# case = []
# th_arr = [0 for _ in range(th)]
#
# # th가 1인 경우는 따로 구함
# th_arr[0] = sum(numbers)
# index = 0
# for t in range(2, th + 1):
#     # t의 개수만큼 자른다.
#
#
#     # 만약 r이 0이 아닌 경우, 경우의 수를 구한다.
#     min_all = int(1e9)
#     q, r = divmod(N, t)
#     # print(f'q => {q}, r => {r}')
#     for i in range(q + 1):
#         q, r = divmod(N, t)
#         print(f'q => {q}, r => {r}')
#
#         sum_all = 0
#         index = 0
#         if r != 0:
#             case = [th] * i + [r] + [th] * (q - i)
#             print(f' >> 111case is {case}')
#         else:
#             case = [th] * i + [th] * (q-i)
#             print(f' >> 222case is {case}')
#
#         print(f'case = {case}')
#         for c in case:
#             try:
#                 temp = max(numbers[index:index + c])
#             except:
#                 print(f"error is : {index} -> {index + c}")
#                 sys.exit(0)
#             print(f'temp = {temp}')
#             sum_all += temp
#             index = index + c
#
#         print(f'>> sum_all is {sum_all}')
#         min_all = min(min_all, sum_all)
#
#         print(f'>> min_all is {min_all}')
#
#         th_arr[t - 1] = min_all
#
# print(th_arr)
# print(min(th_arr))
