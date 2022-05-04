'''
  n(10진수) -> k진수

    1. k진수 변환
    2. 0이 없는지 확인
     2-1. 없다면 소수 확인 -> 종료
    3. 0이 있다면 0을 기준으로 split
    5. split 리스트 돌면서 소수 판별 -> 맞다면 cnt 증가

    [핵심]
     - 소수 찾는 방법에도 빠른 방법과 메모리를 덜 잡아먹는 방식이 있다.
'''

from math import sqrt


# 소수 판별
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


# 10진수 -> k진수 변환 (진법)
def convert(n, k):
    result = ''

    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)

    return result[::-1]


def solution(n, k):
    cnt = 0

    # 1. k진수 변환
    n = convert(n, k)

    # 2. 0이 없는지 확인
    if n.find('0') == -1:
        # 2-1. 없다면 -> 소수 확인 -> 종료
        n = int(n)
        if n != 1 and is_prime_number(n):
            return 1
        else:
            return 0

    # 3. 0이 있다면 0을 기준으로 split
    else:
        n_list = [x for x in n.split('0') if x != '']

        # 4. split 리스트 돌면서 소수 판별 -> 맞다면 cnt 증가
        for num in n_list:
            if int(num) != 1 and is_prime_number(int(num)):
                cnt += 1

    return cnt


print(solution(437674, 3))
# print(solution(110011, 10))
# print(solution(1, 10))
# print(solution(524287, 2))
