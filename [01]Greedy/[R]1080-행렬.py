import sys

N, M = map(int, input().split())
before_matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
after_matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
count = 0

def convert(x, y, before_matrix):
    for i in range(x, x+3):
        for j in range(y, y+3):
            before_matrix[i][j] = 1-before_matrix[i][j]


for i in range(0, N-2):
    for j in range(0, M-2):
        if before_matrix[i][j] != after_matrix[i][j]:
            count += 1
            convert(i, j, before_matrix)

# 전체 배열 검사
for i in range(0,N):
    for j in range(0,M):
        if before_matrix[i][j] != after_matrix[i][j]:
            print(-1)
            exit()


print(count)

