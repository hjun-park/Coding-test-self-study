import sys

input = sys.stdin.readline

m, n = map(int, input().strip().split(' '))

for i in range(n):
    for j in range(m):
        print('*', end='')
    print(end='\n')
