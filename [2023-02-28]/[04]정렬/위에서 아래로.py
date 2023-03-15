import sys

n = int(sys.stdin.readline().rstrip())

array = []
for i in range(n):
    array.append(sys.stdin.readline().rstrip())

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
