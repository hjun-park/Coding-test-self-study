import sys
from collections import deque

input = sys.stdin.readline

'''
    문제의 핵심 (https://hongcoding.tistory.com/44)
    1) 앞뒤로 괄호가 있는 경우 [1:-1] 로 따로 빼내고 deque를 만들어준다.
    2) "[]" 입력을 받아서 deque 길이는 1이기 때문에 길이가 0이라면 예외사항으로 빈 큐로 초기화 필요
    3) reverse를 할 때 매번 deque를 뒤집어주면 시간초과 나기 때문에 뒤집는 횟수를 count해서 
       홀수 번일 때만 뒤집도록 수정한다.
'''

for _ in range(int(input().rstrip())):
    p_list = list(input().rstrip())
    n = int(input().rstrip())
    x = deque(input().rstrip()[1:-1].split(','))

    rev_count = 0
    flag = False

    # 2) 0이라면 따로 비어있는 deque 생성
    if n == 0:
        x = deque()

    # 3) reverse 하는 것이 아니라 count를 센다. 짝수번은 뒤집지 않아도 된다
    for p in p_list:
        if p == 'R':
            rev_count += 1
        elif p == 'D':
            if len(x) < 1:
                flag = True
                print("error")
                break
            else:
                # 짝수의 경우 뒤집어지지 않았기 때문에 앞에서 빼고, 홀수의 경우 뒤에서 빼준다.
                if rev_count % 2 == 0:
                    x.popleft()
                else:
                    x.pop()

    if not flag:
        if rev_count % 2 != 0:  # 뒤집어진 경우
            x.reverse()
        print("[" + ",".join(x) + "]")
