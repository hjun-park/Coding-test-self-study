import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = [0] + list(map(int, input().split()))
d = [0] * (n + 1)

'''
 1) 테이블 정의
 D[i] = 연속된 i개 선택된 수 중 가장 큰 합
 
 2) 점화식
 d[i] = max(d[i], d[i-1] + nums[i]) // 현재까지의 가장 큰 합과 이전까지 가장 큰 합 + 현재 숫자 비교
 
 3) 초기값
 d[i] = a[i]
'''

# 초기값  생성
for i in range(1, n + 1):
    d[i] = nums[i]

# 점화식
for i in range(1, n + 1):
    d[i] = max(d[i], d[i - 1] + nums[i])

# 1-index이므로 1부터 n까지
print(max(d[1:n+1]))
