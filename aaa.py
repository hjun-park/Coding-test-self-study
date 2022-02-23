# import sys
#
# input = sys.stdin.readline
#
# N = int(input().rstrip())
# sticks = [int(input().rstrip()) for _ in range(N)]
#
# max_height = 0
# cnt = 0
# while sticks:
#     stick = sticks.pop()
#
#     # 이전보다 큰 지 확인 ( 크면 보인다는 의미 )
#     if max_height < stick:
#         cnt += 1
#         max_height = stick
#
# print(cnt)
#
# # # 차재윤 풀이
# # max_high = sticks[-1]
# # cnt = 1
# # for i in range(N-2, -1, -1):
# #     if sticks[i] > max_high:
# #         max_high = sticks[i]
# #         cnt += 1
# #
# # print(cnt)

Code = 1
sql = ''' insert into product values (''' + str(Code) + ''', '스위트바니 여름신상 티셔츠', 23000, 6900, 70, 'F'); '''

sql2 = """insert into product values (
' """ + str(Code) + """ ', '스위트바니 여름신상 티셔츠', 23000, 6900, 70, 'F'); """
print(sql)

