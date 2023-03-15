# import sys
# from collections import deque
#
# L = 3
# dirs = [list(input().split()) for _ in range(L)]
# dirs2 = deque((input().split()) for _ in range(L))
#
# print(dirs)
# print(dirs2)
#
# print(dirs2.popleft())

li = [5, 10, 11]
print(li.count(lambda x: x % 5 == 0))
