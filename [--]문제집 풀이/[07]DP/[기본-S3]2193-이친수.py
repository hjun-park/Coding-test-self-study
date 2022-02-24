import sys

input = sys.stdin.readline

'''
 1) 함수 정의
  D[i] = 0으로 시작하지 않고 1이 두번 연속 나타나지 않는 i자리 이친수의 개수
 
 2) 점화식
  D[1] = 1 (1하나뿐)
  D[2] = 1 (10 하나뿐)
  D[3] = 2 (100, 101)
  D[4] = 3 (1010, 1001, 1000)
  
  => D[i] = D[i-2] + D[i-1]  
  
 
 3) 초기화
  D[1] = 1 
  D[2] = 1 
'''

n = int(input().rstrip())
d = [0] * (n + 2)

d[1] = 1
d[2] = 1

for i in range(3, n + 1):
    d[i] = d[i - 2] + d[i - 1]

print(d[n])
