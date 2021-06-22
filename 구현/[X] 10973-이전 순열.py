# num = int(input())
# lit = list(map(int, input().split()))
#
#
# def logic(lit):
#     n = len(lit) - 1
#     i = n - 1
#     while lit[i] <= lit[i + 1]:
#         i -= 1
#     if i == -1:
#         return True
#     j = n
#
#     while lit[i] <= lit[j]:
#         j -= 1
#     lit[i], lit[j] = lit[j], lit[i]  # 바꿔주기
#     while i + 1 < n:
#         lit[i + 1], lit[n] = lit[n], lit[i + 1]
#         i += 1
#         n -= 1
#
#     return False
#
#
# if logic(lit):
#     print(-1)
# else:
#     print(*lit)
