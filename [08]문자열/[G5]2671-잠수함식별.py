import re
import sys

input = sys.stdin.readline

# (100~1~|01)~
# sounds = list(input().rstrip())
sounds = input().rstrip()
p = re.compile('(100+1+|01)+')

if p.fullmatch(sounds) is not None:
    print("SUBMARINE")
else:
    print("NOISE")
