import sys

input = sys.stdin.readline

n = int(input().rstrip())
d = [0] * (n + 2)

MOD = 10_007

'''
  1) 함수의 정의
   D[i] = 2xi 직사각형을 타일로 채우는 경우의 수
  
  2) 점화식
   i=3 부터 시작하며,
   D[i] = (D[i-1] + D[i-2] * 2)
   
  3) 초기값
   D[1] = 1
   D[2] = 3
'''

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % MOD

print(d[n])
