import sys

input = sys.stdin.readline

'''
    경우의 수
'''
form = input().rstrip()

result = 1
if form:
    result = 26 if form[0] == 'c' else 10
    for i in range(1, len(form)):
        if form[i] == 'c':
            if form[i - 1] == 'c':
                result *= 25
            else:
                result *= 26
        else:
            if form[i - 1] == 'd':
                result *= 9
            else:
                result *= 10
print(result)
