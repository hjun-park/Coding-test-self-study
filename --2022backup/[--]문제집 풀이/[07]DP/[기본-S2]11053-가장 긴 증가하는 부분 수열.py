import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
d = [1] * (N + 2)

'''
    1) 함수의 정의
     D[i] = i개일 때 가능한 갯수
    
    2) 점화식
     

    3) 초기값 설정
     D[0] = 0
     D[1] = 1
     D[2] = 2

'''

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:  # 큰 경우에만 횟수 증가 가능
            d[i] = max(d[i], d[j] + 1)  # 현재 횟수와 비교

print(max(d))
