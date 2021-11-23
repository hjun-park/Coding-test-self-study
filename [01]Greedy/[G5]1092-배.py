import sys

input = sys.stdin.readline

'''
    그리디 사고과정
     1) 나열되어 있는 것들은 정렬을 해 보면 어떤 이점이 있을 지 생각 
'''
N = int(input().rstrip())
crane_weight = list(map(int, input().split()))

M = int(input().rstrip())
box_weight = list(map(int, input().split()))

crane_weight.sort(reverse=True)
box_weight.sort(reverse=True)

# 박스의 최대크기가 크레인 최대 크기보다 크면 연산 불가능
if crane_weight[0] < box_weight[0]:
    print(-1)
    sys.exit(0)

time = 0
while len(box_weight) > 0:
    time += 1
    for crane in crane_weight:
        for i in range(len(box_weight)):
            if crane >= box_weight[i]:  # 화물 옮길 수 있으면 화물 제거 후 다음 크레인으로
                del box_weight[i]
                break

print(time)
