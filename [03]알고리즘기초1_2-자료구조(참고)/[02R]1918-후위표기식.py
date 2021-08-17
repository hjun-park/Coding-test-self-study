import sys

str_list = list(sys.stdin.readline().rstrip())
# str_list = input()
stack = []
res = ''

for s in str_list:
    # 만약 해당 index 값이 alpha 라면 출력
    if s.isalpha():
        res += s
    else:
        if s == '(':        # 우선순위가 제일 높은 경우
            stack.append(s)
        elif s == '*' or s == '/':  # 같은 우선순위인 *, /는 최대한 빼준다.
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(s)    # 현재 문자를 다시 스택에 추가
        elif s == '+' or s == '-' : # '+' '-'는 더 낮은 우선연산자가 없어서 자신보다 높은 ( 만날 때까지 추가
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.append(s)
        elif s == ')':  # 괄호가 닫히면 그 사이의 우선순위가 높기 때문에 열린괄호를 만날 때까지 추가
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()
print(res)


