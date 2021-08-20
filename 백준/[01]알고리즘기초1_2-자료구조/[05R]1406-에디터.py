import sys

l_stack = list(sys.stdin.readline().rstrip())
r_stack = []
num = int(input())

for _ in range(num):
    cmd = sys.stdin.readline().rstrip()
    if cmd[0] == 'L':
        # 커서가 맨 왼쪽의 경우 아무런 행동도 하지 않음
        if l_stack:
            r_stack.append(l_stack.pop())
    elif cmd[0] == 'D':
        # 커서가 맨 오른쪽의 경우 아무런 행동도 하지 않음
        # 커서가 적당한 위치에 있을 경우 오른쪽 하나만 빼서 왼쪽으로 이동시킨다.
        # 그렇게 하면 커서가 오른쪽으로 가는 것을 표현할 수 있다.
        if r_stack:
            l_stack.append(r_stack.pop())
    elif cmd[0] == 'B':
        if l_stack:
            l_stack.pop()
    else:
        l_stack.append(cmd[2])  # 리스트가 아닌 문자열이기 때문에 3번째 값을 뽑음


# pop을 하고 append하게 되면 맨 뒤 값이 맨 앞으로 오기 때문에 마지막은 reversed
print(''.join(l_stack + r_stack[::-1]))
