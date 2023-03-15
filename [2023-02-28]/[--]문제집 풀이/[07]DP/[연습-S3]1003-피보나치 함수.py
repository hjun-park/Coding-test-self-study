import sys

input = sys.stdin.readline

d = [[0] * 2 for _ in range(42)]

N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]
max_num = max(nums)

# for _ in range(int(input().rstrip())):
#     num = int(input().rstrip())


'''
 # 함수 정의
  D[i][j] = i번쨰 호출 시 j 숫자가 출력되는 횟수
  
  D[1][0] = 1번째 피보나치 호출 시 0이 출력되는 횟수
  D[1][1] = 1번째 피보나치 호출 시 1이 출력되는 횟수  
 
 # 점화식
  D[i][0] = D[i-2][0] + D[i-1][0]
  D[i][1] = D[i-2][1] + D[i-1][1]
 
 # 함수 초기화
   D[0][0] = 1, D[0][1] = 0
   D[1][0] = 0, D[1][1] = 1
   
   D[2][0] = 1, D[2][1] = 1
   
   D[3][0] = 1, D[3][1] = 2
   
'''

d[0][0] = 1
d[0][1] = 0

d[1][0] = 0
d[1][1] = 1

for i in range(2, max_num + 1):
    d[i][0] = d[i - 2][0] + d[i - 1][0]
    d[i][1] = d[i - 2][1] + d[i - 1][1]

for n in nums:
    print(d[n][0], d[n][1])
