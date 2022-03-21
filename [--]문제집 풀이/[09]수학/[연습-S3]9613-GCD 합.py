import sys

input = sys.stdin.readline


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


for _ in range(int(input().rstrip())):
    result = 0
    numbers = list(map(int, input().split()))
    N = numbers.pop(0)

    # 가능한 모든 쌍의 GCD 연산 합을 구함
    for i in range(N):
        for j in range(i + 1, N):
            gcd_num = GCD(numbers[i], numbers[j])
            result += gcd_num

    print(result)
