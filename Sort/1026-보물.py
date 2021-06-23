import sys

'''
    A[0] * B[0] + ... 
    
    1. S를 최소로 하기 위한 A 재배열
    2. B에 있는 수는 재배열 절대 금지
'''

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

S = 0   # minimize value
for i in range(n):
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(S)

