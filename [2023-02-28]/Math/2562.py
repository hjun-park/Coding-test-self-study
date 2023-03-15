import sys

max_num = 0
max_index = 0

data = list(int(sys.stdin.readline().rstrip()) for _ in range(9)) # 여러 개 문장


for i, num in enumerate(data):
    if max_num < num:
        max_num = num
        max_index = i+1

print(max_num)
print(max_index)
