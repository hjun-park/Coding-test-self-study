# 계수정렬 ( 0 및 양의 정수가 있을 때만 가능 )
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')
