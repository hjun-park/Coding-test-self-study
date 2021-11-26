def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def solution(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        temp = lcm(temp, arr[i])

    return temp
