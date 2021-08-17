import sys
import string

# 소문자, 대문자, 숫자, 공백
print(ord(' '))
for _ in range(100):
    lo, up, nu, bl = 0, 0, 0, 0
    str_list = list(sys.stdin.readline())
    for s in str_list:
        if 48 <= ord(s) <= 57:
            nu += 1
        elif 65 <= ord(s) <= 90:
            up += 1
        elif 97 <= ord(s) <= 122:
            lo += 1
        elif ord(s) == 32:
            bl += 1

    print(lo, up, nu, bl)

