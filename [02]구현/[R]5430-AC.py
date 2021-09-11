import sys

input = sys.stdin.readline


# ==========================================
# 정답 코드
#  - 삭제와 순서 뒤집기는 실제로 하는 것이 아님
#  - 실제로 한다면 시간초과
#  - 
# ==========================================



# ===========================================
# 시간 초과 났던 코드
# ===========================================
# T = int(input())
# for _ in range(T):
#     # p_list = list(map(str, input().rstrip()))    # 함수 순서
#     p_list = input()  # 함수 순서
#     n = int(input())   # 배열에 들어있는 수
#
#     if len(p_list) + n > 700000:
#         print('error')
#         sys.exit(0)
#
#     num_list = input().rstrip()[1:-1].split(',')
#
#     is_error = False
#     for p in p_list:
#         if p == 'R':
#             num_list = num_list[::-1]
#
#         elif p == 'D':
#             if len(num_list) == 0:
#                 is_error = True
#                 break
#             num_list.pop(0)
#
#     if not is_error:
#         print("[" + ",".join(num_list) + "]")
#         # print(list(map(int, num_list)))
#     else:
#         print('error')
