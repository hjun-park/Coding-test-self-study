import sys

input = sys.stdin.readline

n = int(input().rstrip())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(data[i])):
        if j == 0:  # 제일 왼쪽의 값은 왼쪽 대각선이 없음
            data[i][j] += data[i - 1][j]
        elif j == len(data[i]) - 1:  # 제일 오른쪽 값은 오른쪽 대각선이 없음
            data[i][j] += data[i - 1][j - 1]
        else:
            # 점화식, 왼쪽 및 오른쪽 위 대각선을 가지고 처리
            data[i][j] += max(data[i - 1][j - 1], data[i - 1][j])

print(max(data[n - 1]))


