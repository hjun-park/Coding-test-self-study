import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
idx = list(map(int, input().split()))
arr = deque([x for x in range(1, N + 1)])
cnt = 0

for i in idx:
    while True:  # 특정 수를 찾을 때까지 rotate 해야 하므로
        if i == arr[0]:  # 찾는 수라면
            arr.popleft()
            break
        else:
            if arr.index(i) <= len(arr) // 2:  # 왼쪽으로 rotate하는 것이 더 빠른 경우
                arr.rotate(-1)
                cnt += 1
            else:
                arr.rotate(1)
                cnt += 1
print(cnt)
