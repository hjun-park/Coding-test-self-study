def solution(n):
    _str = ''
    while n > 0:
        if n % 3:  # 3으로 나누어 떨어지지 않는 경우는 그대로 진행
            _str += str(n % 3)
            n //= 3
        else:  # 3으로 나누어 떨어지는 경우는 마지막 '4'가 꼭 들어가고 n을 3 나눈 값에 1을 빼줌
            _str += '4'
            n = n // 3 - 1

    return _str[::-1]


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))

# 3진법
# 1 -> 1
# 2 -> 2
# 3 -> 10
# 4 -> 11
# 5 -> 12
# 6 -> 20
# 7 -> 21
# 8 -> 22
# 9 -> 30
