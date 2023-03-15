import sys

input = sys.stdin.readline

a = int(input().rstrip())
for i in range(a):
    p = list(input().rstrip())
    n = int(input().rstrip())
    # stack = deque((input().rstrip()[1:-2]).split(','))
    try:
        stack = list(map(int, (input().rstrip()[1:-1]).split(',')))
    except ValueError:
        stack = []

    # print(stack)

    for op in p:
        if op == 'R':
            stack = stack[::-1]
        elif op == 'D':
            if len(stack) == 0:
                print('error')
                break
            else:
                stack.pop(0)
    else:
        print('[' + ','.join(map(str, stack)) + ']')
