import sys
import string

str_list = list(sys.stdin.readline().rstrip())
alpha = string.ascii_lowercase
result = []

for i in str_list:
    if i.islower():
        index = (alpha.index(i) + 13) % 26
        result.append(alpha[index])
    elif i.isupper():
        i = i.lower()
        index = (alpha.index(i) + 13) % 26
        result.append(alpha[index].upper())
    else:
        result.append(i)

for i in result:
    print(i, end='')
