import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

array.sort()


# 산술평균
print(round(sum(array) / n))

# 중앙값
print(array[n // 2])

# 최빈값
c = Counter(array)
mode = c.most_common()

if len(mode) > 1:
    if mode[0][1] == mode[1][1]:  # 최빈값이 여러개인 경우
        print(mode[1][0])  # 두 번째로 작은 값 출력
    else:
        print(mode[0][0])
else:
    print(mode[0][0])

# 범위
print(array[-1] - array[0])

