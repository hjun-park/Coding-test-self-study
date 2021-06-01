import sys

# 아이디어,
# # 이차원 배열로 한 번에 입력받기보다 각 행 하나씩 입력받은 후 비교처리

n, m = map(int, sys.stdin.readline().split())

max_value = -1
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    if max_value <= min(data):
        max_value = min(data)

print(max_value)


