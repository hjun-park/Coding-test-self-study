import sys

input = sys.stdin.readline

_str = input().rstrip()
alpha = ['U', 'C', 'P', 'C']

i = 0
for a in alpha:
    if a in _str:
        i += 1
        _str = _str[_str.index(a) + 1:]  # 해당 문자열이 발견된 그 이후 시점만을 자름
    else:
        print('I hate UCPC')
        break
if i == 4:
    print('I love UCPC')
