import sys

array = list(map(int, sys.stdin.readline().rstrip()))

count = [0] * 10
result = []

for i in range(len(array)):
    count[int(array[i])] += 1

for i in range(len(count)):
    for j in range(count[i]):
        result.append(i)

result.reverse()

for i in result:
    print(i, end='')