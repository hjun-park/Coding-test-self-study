import sys

x = int(input())
dp_table = [0] * 300001  # 계산된 결과를 저장하기 위한 DP 테이블 초기화

'''
    dp_table[x의 값] = 연산횟수
'''

for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우 ( 1을 더한건 연산 횟수 즉, 함수 호출 횟수를 구하기 위함 )
    dp_table[i] = dp_table[i - 1] + 1

    # dp_table에 있는 기존 연산 수와 값에 2를 나눈 결과의 연산 수 비교,
    # 가장 최소 값이 연산횟수 결과값으로 들어감
    # -> -1빼기, 2, 3, 5 나눈 수 중 가장 작은 값이 나온 연산횟수로 집어넣으려고 함
    if i % 2 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)

    if i % 3 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)

    if i % 5 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 5] + 1)

print(dp_table[x])
