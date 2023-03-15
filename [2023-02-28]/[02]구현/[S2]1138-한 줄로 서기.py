import sys

input = sys.stdin.readline

N = int(input().rstrip())
index = list(map(int, input().split())) # 키가 1인 사람부터해서 자기 앞 사람 몇명인지 있는 값
result = [0] * N

'''
    핵심: index를 순회하면서 결과값 인덱스 하나하나 비교하며 어디에 집어넣을 지 본다.  
'''

for height in range(N): # 키를 1씩 증가시킴 ( index를 순회하는 것과 동일 )
    count_zero = 0

    for rs in range(N):  # 결과값 인덱스 0부터 끝까지 돌면서 어디에 집어넣을 지 결정한다.
        if count_zero == index[height] and result[rs] == 0:  # 넣으려는 위치가 0이고, 자기 앞 사람이 index[height] 인원만큼 있는 경우
            result[rs] = height + 1  # 넣으려는 위치에 자기 키를 집어넣음
            break
        elif result[rs] == 0:  # 넣으려는 위치 값이 0이지만 count_zero 수가 맞지 않은 경우
            count_zero += 1
        else:  # 전혀 비교점이 없는 경우는 그냥 넘어감
            pass

print(*result)
