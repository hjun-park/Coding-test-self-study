import sys

# 메모이제이션화 하기 위한 리스트 초기화
d = [0] * 100


# 피보나치 함수를 재귀함수로 구현
def fibo(x):
    # 1) 종료 조건 :: x가 1 혹은 2일 때 1을 반환
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적이 있다면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 계산한 적이 없다면 점화식에 따른 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))
