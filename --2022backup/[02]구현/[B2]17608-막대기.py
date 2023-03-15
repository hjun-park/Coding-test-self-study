import sys

input = sys.stdin.readline

N = int(input().rstrip())
height = [int(input().rstrip()) for _ in range(N)]

max_height = 0

cnt = 0
while height:
    element = height.pop()

    # 이전보다 더 큰게 보이면 보인다는 얘기
    if max_height < element:
        cnt += 1
        max_height = element  # 갱신

print(cnt)
