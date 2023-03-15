import re
import sys

input = sys.stdin.readline

'''
    [요약]
    1. 반지는 대문자 10개 
    2. 문자열을 포함하는 반지는 몇 개 인지?
        
    [풀이]
    1. 입력 후 리스트 합치고 정규표현식 추출 
    
    [주의점]

'''

cnt = 0
p = re.compile(input().rstrip())
for _ in range(int(input().rstrip())):
    ring = input().rstrip()
    ring += ring
    
    if re.search(p, ring) is not None:
        cnt += 1

print(cnt)
