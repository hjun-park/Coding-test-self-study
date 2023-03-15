import sys

input = sys.stdin.readline

while True:
    M, A, B = map(int, input().split())

    if M == 0 and A == 0 and B == 0:
        sys.exit(0)

    time = round(abs(3600 * (M / A) - (3600 * (M / B))))
    time, second = divmod(time, 60)
    hour, minute = divmod(time, 60)

    print(f'{hour}:{minute:02}:{second:02}')
