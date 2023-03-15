import sys

input = sys.stdin.readline

'''
1. 괄호가 올바른 형식인지 검증   -> check_brackets() 
2. 괄호가 올바른 형식이 검증 되었다면 괄호에 따라 연산 () => 2점 [] => 3점  -> calc_brackets()
'''


def check_brackets(ss):
    stack = []

    for s in ss:
        if s == '(' or s == '[':  # 여는 괄호라면 stack 집어넣기
            stack.append(s)
        elif stack and s == ')':  # 닫힌 괄호 & 스택 비어있지 않음
            if stack[-1] == '(':  # 괄호 쌍이 맞는 경우
                stack.pop()
            else:  # 괄호 쌍이 다른 경우
                stack.append(s)
        elif stack and s == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
        else:  # 그 어느 것도 속해 있지 않거나 열린 괄호가 없는데 닫힌 괄호를 바로 만난 경우
            stack.append(s)

    # 스택에 값이 있으면 유효한 괄호 쌍이 아님
    return False if stack else True


def calc_brackets(ss):
    stack = []

    # 괄호 순회
    for s in ss:
        # 여는 괄호 만나면 stack에 추가
        if s == '(' or s == '[':
            stack.append(s)

        # 닫힌 괄호 만나면
        elif s == ')':
            # 직전괄호 확인해서 여는 괄호라면 2나 3으로 치환
            if stack[-1] == '(':
                stack[-1] = 2
            # 그렇지 않으면 거꾸로 순회해서
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    # 만약 여는 괄호를 만났다면 tmp에 2를 곱해서 집어 넣어준다.
                    if stack[i] == '(':
                        stack[i] = tmp * 2
                        break
                    # 그렇지 않으면 계속 더해나가고 pop하고를 반복한다.
                    else:
                        tmp += stack[i]
                        stack.pop()

        # 닫힌 괄호 만나면 (2)
        elif s == ']':
            # 직전괄호 확인해서 여는 괄호라면 2나 3으로 치환
            if stack[-1] == '[':
                stack[-1] = 3
            # 그렇지 않으면 거꾸로 순회해서
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    # 만약 여는 괄호를 만났다면 tmp에 2를 곱해서 집어 넣어준다.
                    if stack[i] == '[':
                        stack[i] = tmp * 3
                        break
                    # 그렇지 않으면 계속 더해나가고 pop하고를 반복한다.
                    else:
                        tmp += stack[i]
                        stack.pop()

    return sum(stack)


brackets = list(input().rstrip())

if check_brackets(brackets) is False:
    print(0)
    sys.exit(0)
else:
    print(calc_brackets(brackets))
