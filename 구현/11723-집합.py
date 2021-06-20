import sys

m = int(sys.stdin.readline().rstrip())
s = set()

for _ in range(m):
    # 명령행 인자는 1개 혹은 2개가 들어옴
    temp = sys.stdin.readline().rstrip().split()

    # 1인 경우는 all 아니면 empty
    if len(temp) == 1:
        if temp[0] == "all":
            s = set([x for x in range(1, 21)])
        else:   # empty가 오는 경우
            s = set()

    else:
        func, x = temp[0], temp[1]  # 명령행인자 / 숫자
        x = int(x)

        if func == "add":
            s.add(x)
        elif func == "remove":
            s.discard(x)
        elif func == "check":
            print(1 if x in s else 0)
        elif func == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)


