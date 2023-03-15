from math import sqrt


# 약수 구하기
def find_divisor(n):
    divisor = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != (n // i):
                divisor.append(n // i)

    return len(divisor)


def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        if find_divisor(n) % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer


print(solution(13, 17))
print(solution(24, 27))
