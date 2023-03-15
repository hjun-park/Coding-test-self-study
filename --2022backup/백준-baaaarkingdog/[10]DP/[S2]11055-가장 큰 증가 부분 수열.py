import sys

input = sys.stdin.readline

N = int(input().rstrip())                   # 숫자 개수
A = [0] + list(map(int, input().split()))   # 배열

d = [0] * (N+2)                             # DP 초기화
d[1] = A[1]                                 # for문에서 A[i] A[j] 타기 위해 초깃값 설정


for i in range(1, N+1):                     # 1부터 N까지
    for j in range(1, i+1):                 # 1부터 i까지 진행 하면서
        if A[j] < A[i]:                     # 이전 값 보다 큰 경우에만 연산 진행
            d[i] = max(d[i], d[j] + A[i])   # 이전 값 보다 크다면 d[j]와 현재값인 A[i] 더한다. (d[j]는 이전 j인덱스까지 증가하는 숫자들의 합이라고 당연히 생각하기)

print(max(d))
