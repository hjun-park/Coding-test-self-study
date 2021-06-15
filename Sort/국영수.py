import sys

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(str, input().split())))

# data = sorted(data, key=lambda a: a[1], reverse=True)
# data = sorted(data, key=lambda a: a[2])
# data = sorted(data, key=lambda a: a[3], reverse=True)
# data = sorted(data, key=lambda a: str.upper(a[0]))

# 더 쉬운 방법 - 한 줄로 정렬이 가능하다.
data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for user in data:
    print(user[0])

