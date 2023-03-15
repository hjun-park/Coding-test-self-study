import sys

input = sys.stdin.readline

N = int(input().rstrip())
d = [0] * N

'''
    d[n] => n번째 와인까지 따졌을 때 마실 수 있는 최대 와인 양
    
    1) [현재 + 이전] 이전 와인을 마시는 경우 ( 현재 + 이전 + 전전전 포도주 총량 )
     -> (wine[i] + wine[i-1] + d[i-3])
     
    2) [현재] 이전 와인은 마시지 않는 경우 ( 현재 + 전전 포도주 총량)
     -> (wine[i] + d[i-2])
     
    3) [ ] 현재 포도주 마시지 않는 경우 ( 전 포도주까지의 총량 )
     -> d[i-1]
     
     위 3개 경우에 대해서 max값을 구해준다.
'''

wines = []
for _ in range(N):
    wines.append(int(input().rstrip()))

d[0] = wines[0]
if N > 1:
    d[1] = wines[0] + wines[1]

if N > 2:
    d[2] = max(wines[2] + wines[1], wines[2] + wines[0], d[1])

for i in range(3, N):
    d[i] = max(wines[i] + wines[i - 1] + d[i - 3], wines[i] + d[i - 2], d[i - 1])

print(d[N - 1])
