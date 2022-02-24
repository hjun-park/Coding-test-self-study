import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))  # 1-index 사용하므로 [0] 패딩 추가
d = [0] * 100004

'''
    prefix sum 이용
    
    D[i] = A[1] + A[2] + ... + A[i]
    D[i] = D[i-1] + A[i]
'''

# 1-indexed
d[0] = 0

for i in range(1, N + 1):
    d[i] = d[i - 1] + a[i]  # 자기자신과 그 이전 수까지의 더한 값

for i in range(M):
    start, end = map(int, input().split())
    print(d[end] - d[start - 1])  # end까지의 합에서 start 이전까지의 합을 빼면 구간합이 나온다.
