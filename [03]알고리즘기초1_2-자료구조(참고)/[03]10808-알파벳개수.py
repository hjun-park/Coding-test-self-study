import sys
from collections import Counter

str_list = list(sys.stdin.readline().rstrip())
count_list = Counter(str_list)
# count_list = sorted(count_list)

for i in range(ord('a'), ord('{')):
    result = count_list.get(chr(i))
    if result is None:
        print('0', end=' ')
    else:
        print(result, end=' ')

