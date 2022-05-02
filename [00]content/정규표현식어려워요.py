import re

# [참고 링크]
# https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/07/21/regex-usage-02-basic/

'''
01. 문자열을 찾는 함수
'''
re.match('a', 'aaa')  # 처음부터 확인하며 index 반환 없을 시 None 반환
re.search('a', 'aaa')  # 위치와 상관없이 검색하여 index 반환 없을 시 None 반환
re.findall('a', 'aaa')  # 모든 문자열 검색하여 list 반환 없을 시 empty list 반환
re.fullmatch('a', 'aaa')  # 모든 문자열이 일치해야만 index 반환 없을 시 None 반환
re.sub('[^a-z\d\-\_\.]', '', 'abcabcabcabcabcabc')  # [^] 의미는 '제외' 뜻임
[re.split(r"([0-9]+)", f) for f in files]  # 찾아보니 나온 더 쉬운 방법

re.search('match', "'matchObj'").group()  # group()을 이용하면 문자열을 뽑을 수 있다.

'''
02. 특수문자
'''

# [] => 여러 문자 중 하나라도 일치하면 매칭 (OR)
re.fullmatch("You[;']re studying re module[.,]", 'You;re studying re module,')  # 매칭 된다.

# . => 모든 문자와 일치
re.findall('r..n[.]', 'ryan. ruin rain round. reign')

'''
03. re.match(pattern, strings, flags) 에서의 flags 옵션
'''
re.match('a', 'aaa', re.IGNORECASE)  # 대소문자 구분없이 일치
re.match('a', 'aaa', re.ASCII)  # 대소문자 구분없이 일치
re.match('a', 'aaa', re.UNICODE)  # 대소문자 구분없이 일치

'''
04. 문자 집합 : \w \W, \d \D, \s \S, \b \B

\w : [단어] 영어대소문자, 숫자, 언더바
\W : [단어이외] 공백 문자, 특수 문자
\d : [숫자] 숫자 1개
\D : [비숫자] 비 숫자 1개
\s : 공백 문자
\S : 비 공백 문자
\b : 단어와 비 단어 사이 추출
\B : 비 단어와 단어 사이 추출
'''

# line과는 정확히 일치하는 문자, 'outline' 'linear' 과는 일치하지 않아야 함
re.match('\bline\b', 'line')
re.match('\bline\b', 'outline')

# stacatto 에는 일치하지만 'cat', 'catch', 'copycat'와는 일치하지 않음
re.match('\Bcat\B', 'cat')
re.match('\Bcat\B', 'copycat')

'''
05. 행의 시작이나 끝의 대상을 강조

\A : 문자열의 시작
\Z : 문자열의 끝
^ : 행 시작
$ : 행 끝 
'''

print(re.findall('\Aryan\d\Z', 'ryan1'))

# 검출되지 않음
print(re.findall('^ ryan\d\s$', ' ryan1 \n ryan2 \n rain1 \n ryan3 '))

# \n 전후로 행의 시작과 끝이 여러 개가 있는데, 모두 찾아내는 것
print(re.findall('^ ryan\d\s$', ' ryan1 \n ryan2 \n rain1 \n ryan3 ', re.MULTILINE))

'''
06. 정규표현식 : OR, 반복
'''
# '|' => one, two, three 중 하나라도 대응시키기 위함 ( 대응되면 list로 반환 )
print(re.findall('one|two|three', 'one four two three zero'))

# '*' => 0회 이상 반복
print(re.findall('a*', 'aaabaaa aa  '))  # ['aaa', '', 'aaa', '', 'aa', '', '', '']

# '+' => 1회 이상 반복
print(re.findall('a+', 'aaabaaa aa  '))  # ['aaa', 'aaa', 'aa']

# {a, b} => a회 이상 b회 이하 반복
print(re.findall('a{2,4}', 'a aa aaa aaaa aaaaa'))  # ['aa', 'aaa', 'aaaa', 'aaaa']

# '?' => 0회 or 1회 반복
print(re.findall('ab?a', 'aa aba aaaa'))  # ['aa', 'aba', 'aa', 'aa']

'''
07. 그룹, 캡처
'''

# 그룹화를 하기 전
print(re.findall('12+', '12 1212 1222'))  # ['12', '12', '12', '1222']

# '()' => 그룹화 진행 후 1212 만 찾아냄
print(re.fullmatch('(12)+', '1212'))
print(re.findall('(12)+', '1212'))  # ['12'] => findall만 12로 찾아짐 (캡처 때메 그렇다)

# 캡처 - 원하는 부분만 추출 (소괄호 이용하면 된다)
print(re.findall('\d{4}-(\d\d)-(\d\d)', '2028-07-28'))  # [('07', '28')]

'''
08. 치환
'''
print(re.sub('\d{4}', 'XXXX', '010-1234-5678'))  # 010-XXXX-XXXX

# 치환을 이용한 HTML 태그 제거
result = re.split('<[^<>]*>',
                  '<html> Wow <head> header </head> <body> Hey </body> </html>')
result = list(map(lambda x: x.strip(), result))
result = list(filter(lambda x: x != '', result))
print(result)

'''
09. 정규표현식 예제
'''
# https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/08/06/regex-usage-07-example/
