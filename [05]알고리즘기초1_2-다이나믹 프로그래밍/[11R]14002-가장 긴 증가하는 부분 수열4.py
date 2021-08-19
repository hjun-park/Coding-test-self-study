import sys

# N = int(input())
# num_list = list(map(int, sys.stdin.readline().split()))
#
# num_set = set(num_list)
#
# print(len(num_set))

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

d = [1] * (N + 1)

for i in range(N):  # 수열의 크기만큼 순회
    for j in range(i):  # i만큼 순회 ( 1,1 -> 2,1 -> 2,2 -> )
        if num_list[i] > num_list[j]:  # 현재 위치(i)보다 이전 위치 j가 작은지 확인
            # 존재한다면 현재 d[i]에 있는 값과 이전위치값 d[j] + 1 비교한다. 그리고 갱신한다.
            d[i] = max(d[i], d[j] + 1)

print(max(d))

# 출력은 뒤에서부터 순차적으로 진행한다.
order = max(d)

result = []
for i in range(N - 1, -1, -1):
    if d[i] == order:   # 가장 큰 순서라면
        result.append(num_list[i])  # 먼저 출력
        order -= 1  # 순서 감소
result.reverse()

# order = min(d)
# for i in range(0, N+1):
#     if d[i] == order:   # 가장 큰 순서라면
#         result.append(num_list[i])  # 먼저 출력
#         order += 1  # 순서 감소


for i in result:
    print(i, end=' ')
