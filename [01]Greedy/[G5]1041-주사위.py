import sys

input = sys.stdin.readline

N = int(input().rstrip())
dices = list(map(int, input().split()))

result = 0
min_list = []

'''
    https://710jym.medium.com/baekjoon-1041-python-4153e686aec4
    1) 주사위를 유심히 살펴보고 공식을 내는 것이 중요 (어려움)
'''

# 주사위가 1개인 경우 나머지 5개 면은 순서대로 더하면 된다.
if N == 1:
    dices.sort()
    for i in range(5):
        result += dices[i]

else:
    # 1) 주사위 서로 마주보는 면 중 가장 작은 값 등록
    min_list.append(min(dices[0], dices[5]))
    min_list.append(min(dices[1], dices[4]))
    min_list.append(min(dices[2], dices[3]))
    min_list.sort()

    # 최솟값으로 쌓아올린 N x N x N 주사위는 결국 어느 면에서 보던지 면 3개만 보이게 된다.
    # 2) 1, 2, 3면 주사위 최솟값 결정
    min1 = min_list[0]
    min2 = min_list[0] + min_list[1]
    min3 = min_list[0] + min_list[1] + min_list[2]

    # 3) N x N x N 주사위에서 보여지는 각 1, 2, 3면의 개수
    n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
    n2 = 4 * (N - 1) + 4 * (N - 2)
    n3 = 4

    result += min1 * n1
    result += min2 * n2
    result += min3 * n3
print(result)




