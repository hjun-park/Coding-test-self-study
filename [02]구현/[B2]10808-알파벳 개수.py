# 두 번째 예시
import sys
from collections import Counter  # Counter 패키지는 리스트 각 원소의 개수를 세는 데 사용

str_list = list(sys.stdin.readline().rstrip())
count_list = Counter(str_list)
# print(count_list) # Counter({'o': 2, 'b': 1, 'a': 1, 'e': 1, 'k': 1, 'j': 1, 'n': 1})

for i in range(ord('a'), ord('{')):
    result = count_list.get(chr(i))
    if result is None:
        print('0', end=' ')
    else:
        print(result, end=' ')

# 최적의 예시
# import sys
# import string
#
# input = sys.stdin.readline
#
# S = list(input().rstrip())
# alpha_dict = dict.fromkeys(string.ascii_lowercase, 0)
#
# for c in S:
#     alpha_dict[c] += 1
#
# print(*alpha_dict.values())
