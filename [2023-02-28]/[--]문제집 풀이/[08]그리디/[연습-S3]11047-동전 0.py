import sys

input = sys.stdin.readline

N, K = map(int, input().split())
value = [int(input().rstrip()) for _ in range(N)]

'''
 [DP 접근]
 D[i] = 가치의 합을 i로 만들 때 필요한 동전 최솟값
 D[i] = min(D[i-A1], D[i-A2] .. ) + 1 
 .. 시간초과
 
 [그리디] 
 - 가장 비싼 동전부터 사용
'''

cnt = 0
for v in value[::-1]:
    q, K = divmod(K, v)
    cnt += q
    if K == 0:
        break

print(cnt)
