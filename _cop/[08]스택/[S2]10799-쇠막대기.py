import sys

input = sys.stdin.readline

ss = list(input().rstrip())
stack = []
cnt = 0
before = ''

for s in ss:
    if s == '(':
        stack.append(s)
    else:  # ')'
        if before == '(':  # 바로 직전이 여는 괄호면 레이저에 의해 막대들이 쪼개짐
            stack.pop()  # 일단 pop 진행
            cnt += len(stack)
        else:  # 바로 직전이 닫힌 괄호라면 막대 길이 증가
            stack.pop()
            cnt += 1
    before = s

print(cnt)
