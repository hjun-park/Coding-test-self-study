import sys
from collections import deque

N = int(input())
num_list = list(map(int, sys.stdin.readline().rstrip().split())) # seq

stack = deque()
result = [-1] * N   # oh_big

for i in range(N):
    # 만약 배열에서 스택 끝 부분[-1]에 있는 값[0]보다 큰 경우가 있다면
    while stack and (stack[-1][0] < num_list[i]):
        tmp, idx = stack.pop()  # 뽑아내고
        result[idx] = num_list[i]   # 오큰수를 해당 num_list[i]의 값으로 교체
    stack.append([num_list[i], i])

print(*result)
