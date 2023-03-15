import re
import sys

input = sys.stdin.readline

'''
  # 파이썬 정규표현식 [https://wikidocs.net/4308]
  p = re.compile('ab*') # 컴파일하여 작업 수행하기 위한 객체 생성
  m = p.match("python") # 처음부터 정규식과 매칭되는지 확인
  s = p.search("python") # 문자열 전체를 검색하여 정규식과 매치되는지 검색
  이외에도 findall, findmatch가 있다.
  
  ** 핵심은 전체 매칭되는 것을 찾아야하므로 full match를 이용해야 한다.
  ( https://nerogarret.tistory.com/30 )
'''

'''
    (100+1+ | 01)+
'''

p = re.compile('(100+1+|01)+')
for _ in range(int(input().rstrip())):
    nums_list = list(input().rstrip())
    nums_str = ''.join(nums_list)

    if p.fullmatch(nums_str) is not None:
        print('YES')
    else:
        print('NO')
