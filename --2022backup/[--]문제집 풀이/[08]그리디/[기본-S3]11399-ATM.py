import sys

input = sys.stdin.readline

N = int(input().rstrip())
P = sorted(list(map(int, input().split())), reverse=True)

'''
    문제풀이 아이디어 (가장 큰 수는 제일 나중에 와야 한다.)
    
    1. 정렬
    2. 리스트 순회하며 시간을 더함
'''

time = 0
for i in range(1, (N + 1)):
    time += (P[i - 1] * i)

print(time)
