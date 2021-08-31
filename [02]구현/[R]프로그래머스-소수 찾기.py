import sys
import math

'''
1) 에라토스테네스의 체 
'''


# 소수 판별 함수
def is_prime_number(n):
    # 에라토스 테네스의 체
    # 1) n까지의 모든 수 인덱스 값을 True로 설저
    array = [True for i in range(n + 1)]

    # 2부터 n 제곱근까지만 체크
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:  # 만약 i가 소수인 경우
            # 자기 자신을 제외한 나머지 배수 제거
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1  # 다음 수 체크

    # return [x for x in range(2, n + 1) if array[x]]
    return array[n]

print(is_prime_number(23))
