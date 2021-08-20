import sys

N = int(sys.stdin.readline().rstrip())
dq = []

for _ in range(N):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push_front':
        dq.insert(0, cmd[1])

    elif cmd[0] == 'push_back':
        dq.append(cmd[1])

    elif cmd[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop(0))

    elif cmd[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop(-1))

    elif cmd[0] == 'size':
        print(len(dq))

    elif cmd[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    else:  # back
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
