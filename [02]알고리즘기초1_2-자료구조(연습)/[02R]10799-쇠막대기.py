import sys

'''
1) '('가 나오면 스택에 집어넣는다.
2) ')'가 나올 시
2-1) ')'가 나오고 이전 문자가 바로 '('였으면 '('개수(=쇠막대기 개수)만큼 개수를 더해준다.
2-2) ')'가 나오고 이전 문자도 ')'였으면 쇠막대기 끝의 표시
'''

th = sys.stdin.readline().rstrip()
stack = []
result = 0


for i in range(len(th)):
    if th[i] == '(':    # 쇠막대 시작점,
        stack.append('(')
    else:
        if th[i-1] == '(':  # 레이저인 경우,
            stack.pop() # 이전 것 빼준다.
            result += len(stack)    # 레이저로 모든 쇠막대를 분리함( 쇠막대 수만큼 +)
        else:
            stack.pop()
            result += 1 # 전체적 쇠막대 1개가 만들어지므로 1개 +

print(result)

