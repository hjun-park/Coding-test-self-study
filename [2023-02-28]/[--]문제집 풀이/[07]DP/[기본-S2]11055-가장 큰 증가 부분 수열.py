import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
d = [] + A  # 복사
# d = A[:]

'''
    1. 함수 정의
     D[i] = 점점 늘어나는 수 i를 선택한 것들의 합
     
    2. 점화식 (i보다 이전 값들을 하나하나 비교하는데 A[i]가 A[j]보다 큰 경우에만 적용됨 
     D[i] = max(D[i], D[j] + A[i])
    
    3. 초깃값 선정
     D[i] = A[i] 
    
'''

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            d[i] = max(d[i], d[j] + A[i])

# 그 중에서 가장 큰 값을 반환
print(max(d))
