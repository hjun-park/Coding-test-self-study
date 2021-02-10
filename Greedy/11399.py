N = int(input())
data = list(map(int, input().split()))
min_time = 0

data.sort()
for i in range(N):
    for j in range(i + 1):
        min_time += data[j]

print(min_time)

