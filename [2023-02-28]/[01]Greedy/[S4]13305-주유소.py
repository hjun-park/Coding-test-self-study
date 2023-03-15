import sys

n = int(sys.stdin.readline().rstrip())

road_list = list(map(int, sys.stdin.readline().rstrip().split()))
cost_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 간단한 다른 풀이

# 처음은 무조건 더함
result = 0
current_cost = cost_list[0]

# 마지막 주유쇼까지 탐색
for i in range(n - 1):

    # 현재 있는 주요소 비용보다 탐색한 주유소 비용이 저렴하면
    #   현재 주유소를 이동
    if cost_list[i] < current_cost:
        current_cost = cost_list[i]

    # 이동하면서 찾은 주유소 최소 비용 * 지금까지 탐색한 노드
    result += current_cost * road_list[i]

print(result)

# # 첫 번쨰는 무조건 가야하기 때문에 초기화
# result = road_list[0] * cost_list[0]
# current_cost = cost_list[0]
# distance = 0
#
# # 두 번쨰 노드부터 greedy 시작
# for i in range(1, n-1):
#     # 지금 주유소의 주유가격보다 해당 주유소의 주유가격이 작은 경우
#     # 지금까지 왔던 거리와 지금 최소의 주요 가격을 곱해서 결과에 더한다.
#     # 이후 current_cost를 cost_list[i]로 변경한다.
#     if cost_list[i] < current_cost:
#         result += current_cost * distance # 지금까지 왔던 거리와 작은 주요소 비용 곱하고 더함
#         distance = road_list[i] # 현재 위치를 이동
#         current_cost += cost_list[i]
#     else:  # 그렇지 않을 경우 거리만 더해준다.
#         distance = road_list[i]
#
#     if i == n-2: # 마지막일 때 최종 거리까지의 가격 계산
#         result += current_cost * distance
#
# print(result)
