import sys

input = sys.stdin.readline

'''
 1) 테이블 정의
  - dp[i] = i를 1, 2, 3 의 합으로 나타내는 방법의 수 

 2) 점화식 찾기
  - 영상 참고 ( 이런데서도 이런 규칙을 만드는구나 ) 
  - d[4] = d[3] + d[2] + d[1]

 3) 규칙 만들기
 - d[k] = d[k-1] + d[k-2] + d[k-3]

 4) 초깃값 설정
  - d[1] = 1, d[2] = 2, d[3] = 4
'''

# 더 효율적인 방법은 구하고자 하는 가장 큰 n을 선정해서 거기까지 미리 다 구하는 것
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]

    print(d[n])
