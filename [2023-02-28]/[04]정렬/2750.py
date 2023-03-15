import sys

n = int(input())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))    # sys로 입력받아야 훨씬 빠름
    # array.append(int(input()))

array = sorted(array)

for i in array:
    print(i, end='\n')

