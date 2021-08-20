import sys

data = sys.stdin.readline().rstrip()

count0 = 0  # 전부 0으로
count1 = 0  # 전부 1로

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 요소부터 확인
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1


print(min(count0, count1))




