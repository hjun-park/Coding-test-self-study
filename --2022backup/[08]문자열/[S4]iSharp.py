import sys

input = sys.stdin.readline

string = input().rstrip()
string_list = string.split()

common = string_list[0]
del string_list[0]

for s in string_list:
    st = s.replace(',', '')
    string = st.replace(';', '')

    print(common, end='')
    # 특수문자의 경우 뒤에서 출력
    for i in range(len(string) - 1, -1, -1):
        if not string[i].isalpha():  # 알파벳이라면 띄어쓰기
            if string[i] == '[':
                print(']', end='')
            elif string[i] == ']':
                print('[', end='')
            else:
                print(string[i], end='')

    print(' ', end='')

    # 알파벳 출력
    for i in range(len(string)):
        if string[i].isalpha():
            print(string[i], end='')

    print(';')
