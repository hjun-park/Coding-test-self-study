import sys

input = sys.stdin.readline

N = int(input().rstrip())

r, g, b = [0], [0], [0]

for i in range(N):
    t1, t2, t3 = map(int, input().split())

    r.append(t1)
    g.append(t2)
    b.append(t3)

'''
    1) 테이블 정의
     D[i][0] = i번째 집까지 칠할 때 비용 최솟값, 단 i번쨰 집은 빨강
     D[i][1] = i번째 집까지 칠할 때 비용 최솟값, 단 i번쨰 집은 녹색
     D[i][2] = i번째 집까지 칠할 때 비용 최솟값, 단 i번쨰 집은 파랑 
     
    
    2) 점화식 세우기
     D[0][0] = 26
     D[0][1] = 40
     D[0][2] = 83
     D[1][0] = 49+40, 49+83 ==> min
     D[1][1] = 60+26, 60+83
     D[1][2] = 57+26, 57+40
     
     # 즉
     D[k][0] = min(D[k-1][1], D[k-1][2]) + R[k]
     D[k][1] = min(D[k-1][0], D[k-1][2]) + G[k]
     D[k][2] = min(D[k-1][0], D[k-1][1]) + B[k]
    
    3) 초기값 정하기
    D[1][0] = R[1]
    D[1][1] = G[1]
    D[1][2] = B[1]

'''

d = [[0] * 3 for _ in range(N + 1)]
d[1][0] = r[1]
d[1][1] = g[1]
d[1][2] = b[1]

for i in range(2, N + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + r[i]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + g[i]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + b[i]

print(min(d[N][0], d[N][1], d[N][2]))
