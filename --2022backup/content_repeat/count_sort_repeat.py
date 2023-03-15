import sys

# count sort는 양수이고 일정 크기 아래에서는 정말 빠르게 동작하는 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 리스트에서 가장 큰 값까지 커버하는 인덱스를 가진 리스트 선언
count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     # i는 인덱스(0부터 배열길이-1 까지)
#     count[array[i]] += 1    # 몇 개라는 인덱스 표시
#
# for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인 ( 인덱스 사이즈만큼 수행 )
#     for _ in range(count[i]): # 리스트에 기록된 인덱스의 값 만큼 순회함
#         # i는 인덱스 값
#         # j는 필요 없음
#         print(i, end=' ')


# 1. 리스트에서 가장 큰 사이즈보다 1개 더 많은 배열 선언
count = [0] * (max(array) + 1)

# 2. 배열의 수만큼 입력을 받기
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for _ in range()


