import sys

input = sys.stdin.readline

Q, D, N, P = 0, 0, 0, 0

for _ in range(int(input().rstrip())):
    remain = int(input().rstrip())

    Q, remain = divmod(remain, 25)
    D, remain = divmod(remain, 10)
    N, remain = divmod(remain, 5)
    P = remain

    print(Q, D, N, P)
