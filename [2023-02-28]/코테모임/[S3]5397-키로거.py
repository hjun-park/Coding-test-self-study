import sys
from collections import deque

input = sys.stdin.readline

'''
    [요약]
    1) 알파벳 대문자 / 소문자 / 숫자 / 백스페이스 / 화살표
    2) 백스페이스 '-' 만나면 커서 바로 앞 글자를 지운다. (글자가 있다면)
    3) 화살표 '>' '<' 만나면 왼쪽 오른쪽 1씩 움직임 ( 움직일 수 있다면 )
     -> 커서 위치 다음에 문자를 입력하는 구조로 작성

    [풀이과정]
    1. 입력, 커서 초기화
    2. typed 로부터 글자를 하나 뺌
    3. 입력된 값에 따라 처리함
     3-1) 문자인 경우 cur 다음 위치에 password에 대입  // cur 증가
     3-2) 화살표인 경우 cur를 이동 ( 0보다 작거나 len(password)보다 크면 이동 X)
     3-3) 백스페이스를 만나면 cur 위치의 문자열 지움, cur -= 1(cur이 0이라면 continue)
    
'''

T = int(input().rstrip())

for _ in range(T):
    typed = deque(input().rstrip())
    cur = -1
    _len = len(typed)

    password = []

    while typed:
        s = typed.popleft()

        if s.isalpha() or s.isnumeric():
            cur += 1
            password.insert(cur, s)

        # 0보다 클 때만 왼쪽 이동 가능
        elif s == '<':
            cur = (cur - 1) if cur >= 0 else cur

        # len(password)-1 보다 작을 때만 이동 가능
        elif s == '>':
            cur = (cur + 1) if cur < len(password) - 1 else cur

        elif s == '-':
            # 0보다 클 때만 커서를 지울 수 있음
            if cur >= 0:
                password.remove(password[cur])
                cur -= 1

    print(''.join(password))
