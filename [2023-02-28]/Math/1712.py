def calc(A, B, C):
    if B >= C:
        return -1
    else:
        return (A // (C - B)) + 1


if __name__ == '__main__':
    cnt = 0
    A, B, C = map(int, input().split())

    result = calc(A, B, C)
    print(result)
