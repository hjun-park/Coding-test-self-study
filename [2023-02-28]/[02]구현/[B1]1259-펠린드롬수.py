import sys

'''
    1. 숫자로 구성되고 값을 거꾸로 정렬하려면 [::-1] 사용 ( 거꾸로 출력 )
'''

num = sys.stdin.readline().rstrip()

while num != '0':
    if num[::-1] == num:
        print('yes')
    else:
        print('no')

    num = sys.stdin.readline().rstrip()