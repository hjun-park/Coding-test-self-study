'''
    해설지 참고
        https://hjp845.tistory.com/50
        https://westernriver.tistory.com/7

    1. 올바른 괄호 ?
    2. 계산
'''

import sys


# 스택으로 처리할 것이니까 거꾸로 들어가고 먼저 나옴
# 괄호문제 -> 스택으로 해결
def check_brackets(ss):
    stack = []
    for s in ss:
        if s == '(' or s == '[':    # 여는 괄호는 문제 없으므로 무조건 추가
            stack.append(s)
        elif s == ')' and stack:    # 닫힌 소괄호를 만났을 때
            if stack[-1] == '(':    # 끝 요소가 열린 괄호라면 유효한 괄호가 될 수 없음
                stack = stack[:-1]  # stack에서의 pop이라고 생각 ( 맨 끝 요소 제거 )
            else:
                stack.append(s)
        elif s == ']' and stack:    # 위의 경우와 마찬가지
            if stack[-1] == '[':
                stack = stack[:-1]
            else:
                stack.append(s)
        else:
            stack.append(s)
    if stack:                       # 열심히 추가하고 열린/닫힌 괄호 처리해도 남아있다면 유효 x
        return False
    else:
        return True


# 실제 연산이 일어나는 파트
def sol(ss):
    stack = []
    for s in ss:
        # ====================== #
        # # 열린 괄호를 만난 경우 # #
        # ====================== #
        if s == '(' or s == '[':    # 열린 괄호는 일단 추가
            stack.append(s)

        # ====================== #
        # # 닫힌 괄호를 만난 경우 # #
        # ====================== #
        elif s == ')':              # 1) 닫힌 소괄호

            # ====================== #
            # # 닫힌 괄호에서 열린 괄호를 만난 경우 # #
            # ====================== #
            if stack[-1] == '(':    # 여는 괄호가 존재하는 경우
                stack[-1] = 2       # () 상태 => 끝에 하나를 2로 변경
            else:
                tmp = 0
                # 닫힌 괄호인데 리스트 마지막이 숫자이면 그 숫자이전을 확인하여
                # 열린 괄호를 찾을때까지 더해준다.(완벽한 형식이기 때문에 논리가 맞는다)
                for i in range(len(stack) - 1, -1, -1): # 끝 다음에서부터 시작해서 처음 이동
                    if stack[i] == '(':     # 여는 괄호라면 2x
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]

        # ====================== #
        # # 닫힌 괄호를 만난 경우 # #
        # ====================== #
        elif s == ']':              # 2) 닫힌 대괄호

            # ====================== #
            # # 닫힌 괄호에서 열린 괄호를 만난 경우 # #
            # ====================== #
            if stack[-1] == '[':    # 여는 대괄호 존재하는 경우
                stack[-1] = 3       # [] 상태 => 3으로 변경
            else:
                tmp = 0

                # 스택 전체를 돌면서 곱할 수 있는 것들은 곱함
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
    return sum(stack)


# 1) 괄호 입력
input = sys.stdin.readline
brackets = input().strip()

# 2) 유효한 괄호인지 체크
if check_brackets(brackets) is False:
    print(0)
else:   # 3) 유효한 괄호라면 계산 수행
    print(sol(brackets))
