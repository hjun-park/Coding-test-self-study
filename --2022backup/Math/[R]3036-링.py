import sys

N = int(input())
rings = list(map(int, input().split()))

'''
  핵심: 기약분수는 분자, 분모의 최대 공약수로 분자, 분모를 나누어주면 된다.
'''


def gcd(a, b):  # a > b
    while b != 0:  # b가 0이 될 때까지
        remain = a % b
        a = b  # 큰 수는 작은 수로
        b = remain  # 작은 수는 약수로
    return a


for i in range(1, N):  # 둘째 수부터 N번째 ring
    num = gcd(rings[0], rings[i])  # 처음과 나머지 최대공약수 구하기
    print(f'{rings[0] // num}/{rings[i] // num}')

