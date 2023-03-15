import sys

input = sys.stdin.readline

n: int = int(input().rstrip())

nums = [0] + list(map(int, input().split()))

'''
 1) 테이블 정의
 D[i] = 연속된 i개 선택된 수 중 가장 큰 합
 
 2) 점화식
 d[i] = max(d[i], d[i-1] + nums[i]) // 현재까지의 가장 큰 합과 이전까지 가장 큰 합 + 현재 숫자 비교
 
 3) 초기값
 d[i] = a[i]
'''

d = [0] * (n + 2)

# 초기값  생성1
for i in range(1, n + 1):
    d[i] = nums[i]

# 점화식
for i in range(1, n + 1):
    # 이전 꺼를 함께 더하느냐, 현재 값을 그대로 놔두냐
    d[i] = max(d[i], d[i - 1] + nums[i])

print(max(d[1:n + 1]))
