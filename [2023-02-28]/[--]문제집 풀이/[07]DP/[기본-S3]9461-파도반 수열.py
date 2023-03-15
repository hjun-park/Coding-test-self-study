import sys

input = sys.stdin.readline

T = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(T)]
max_num = max(nums)

d = [0] * (max_num + 2)

'''
    1) 함수의 정의
      D[i] = 삼각형 갯수 i개일 때 변의 길이 
      
    2) 점화식
        D[1] + D[4] = 5
        D[2] + D[5] = 7
        D[2] + D[7] = 9
        D[3] + D[9] = 12
        
        D[i] = D[i-1] + D[i-4]
        
        사실 d[i - 2] + d[i - 3];
         
    3) 초기값
     d[1] = 1
     d[2] = 1
     d[3] = 1
     d[4] = 2
     d[5] = 2

'''

d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2

for i in range(6, max_num + 1):
    d[i] = d[i - 1] + d[i - 5]

for num in nums:
    print(d[num])
