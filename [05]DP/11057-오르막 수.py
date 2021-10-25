import sys

input = sys.stdin.readline

N = int(input().rstrip())
d = [[0] * 10 for _ in range(N + 1)]

'''
자릿수 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
1개   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1
2개   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
3개   | 1 | 3 | 6 | 10| 15| 21| 28| 36| 45| 55

여기서 자릿수 3개, 끝자리수 2인 값 (10) 구하는 과정
 => 자릿수 3-1개 짜리를 끝자릿수 2까지 더하면 된다.
 => 식: 1 + 2 + 3 = (6) 

'''

# N이 1인 경우 모든 끝자리수의 오르막수가 1임
for i in range(10):
    d[1][i] = 1

for i in range(2, N + 1):  # N의 개수
    for j in range(10):  # 끝자리 수
        for k in range(j + 1):  # 0부터 끝자리수 +1 까지 모든 값들을 더해준다.
            d[i][j] += d[i - 1][k]

print(sum(d[N]) % 10007)
