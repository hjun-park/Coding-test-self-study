import sys
import string

str_list = list(sys.stdin.readline().rstrip())
alpha_list = string.ascii_lowercase
alpha_dict = dict.fromkeys(alpha_list, -1)


for i, s in enumerate(str_list):
    if alpha_dict.get(s) == -1:
        alpha_dict[s] = i
    else:
        pass


# 만약 키값이 -1이라면 갱신, 키 값이 -1이 아니라면 pass

for s in alpha_dict.values():
    print(s, end=' ')
