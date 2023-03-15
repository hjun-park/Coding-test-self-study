import sys

input = sys.stdin.readline

n = int(input().rstrip())
stack = []
rst = []
is_stack_numbers = True

cnt = 0
for _ in range(n):
    num = int(input().rstrip())

    # 1) 타겟 넘버가 되기 전까지 append, '+' 출력
    # rst에 담아주는 이유는 스택 수열이 되지 못한 경우 출력하면 안 되기 때문
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        rst.append('+')

    # 2) while을 탈출하는 경우는 1부터 세는 cnt가 num과 같다는 의미
    if stack[-1] == num:  # 가장 최근에 집어넣은 값이 num과 같다면 뺄 차례
        stack.pop()
        rst.append('-')
    else:  # cnt가 끝까지 갔는데도 num이 남아 있다면 스택 수열이 되지 못함
        is_stack_numbers = False
        break

if not is_stack_numbers:
    print('NO')
else:
    print('\n'.join(rst))
