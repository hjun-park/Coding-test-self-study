import sys

N = int(input())
d = [[0] * 10 for _ in range(N + 1)]

#
for i in range(1, 10):  # 한 자리수의 경우 1부터 9까지는 모두 1가지 경우의 수
    d[1][i] = 1

MOD = 1000000000

for i in range(2, N + 1):  # 두 자리 이상의 경우에 대해 루프 수행
                           # 세 자리 이상의 수라면 루프를 2번 수행 ( 그 이상은 어차피 똑같음 )
    for j in range(10): # 개수를 누적해가면서 더함
        if j == 0:      # 0 뒤에는 1만 올 수 있다.
            d[i][j] = d[i - 1][1]
        elif j == 9:    # 9 뒤에는 8만 올 수 있다.
            d[i][j] = d[i - 1][8]
        else:   # 2 종류
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

print(sum(d[N]) % MOD)
