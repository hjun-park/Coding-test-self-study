import sys

input = sys.stdin.readline

N = int(input().rstrip())
index = list(map(int, input().split()))
result = [0] * N

'''
    핵심: 0의 갯수를 세어서 적절한 위치를 판단한다.
'''

for i in range(N):
    count_zero = 0

    for j in range(N):  # 0의 위치를 파악하여 적절한 위치에 넣는다.
        if count_zero == index[i] and result[j] == 0:  # 앞에 index[i]개의 0이 있고 넣으려는 위치 result[j]값이 0인 경우
            result[j] = i + 1
            break
        elif result[j] == 0:  # 0이지만 개수가 맞지 않을 경우
            count_zero += 1
        else:  # 전혀 비교점이 없는 경우는 그냥 넘어감
            pass

print(*result)
