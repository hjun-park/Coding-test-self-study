import sys

input = sys.stdin.readline

'''
A - 5
B - 60
C - 10

0. 5로 나누어 떨어지지 않는다면 -1
1. 60으로 나눈 후 나머지는 T에 대입, 몫은 B 증가
2. T에 대해 10으로 나눈 후 나머지는 T에 대입, 몫은 C 증가
3. 나머지는 5로 나누고 몫을 T에 대입


'''


def logic():
    T = int(input().rstrip())
    A, B, C = 0, 0, 0

    if T % 10 != 0:
        print(-1)
        return

    if T >= 300:
        A, T = divmod(T, 300)

    if T >= 60:
        B, T = divmod(T, 60)

    C = T // 10

    print(A, B, C)


logic()
