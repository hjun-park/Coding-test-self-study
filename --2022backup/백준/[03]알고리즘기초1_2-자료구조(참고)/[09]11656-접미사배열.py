import sys

str_list = list(sys.stdin.readline().rstrip())
result = []


for i in range(len(str_list)):
    # print(str_list[i:len(str_list)])
    result.append(''.join(str_list[i:len(str_list)]))


result.sort()

for s in result:
    print(s)
