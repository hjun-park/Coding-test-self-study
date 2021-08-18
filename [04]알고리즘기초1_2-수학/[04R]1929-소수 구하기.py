import sys
import math


def is_prime_number(M, N):
    array = [True for i in range(N + 1)]  # 처음엔 모든 수가 소수인 것으로 초기화

    # 에라토스테네스의 체를 이용
    for i in range(2, int(math.sqrt(N)) + 1):  # 2부터 n제곱근까지 확인
        if array[i] == True:  # i가 소수라면
            # 관련된 모든 배수 제거
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1

    # 소수 리스트만 내보냄
    return [i for i in range(M, N + 1) if array[i]]


M, N = map(int, input().split())

if M == 1:
    M = 2

number = is_prime_number(M, N)

for n in number:
    print(n)
