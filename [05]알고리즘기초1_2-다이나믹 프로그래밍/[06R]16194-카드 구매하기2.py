import sys
INF = int(1e9)

N = int(input())
P = [0] + list(map(int, sys.stdin.readline().split()))
d = [INF] * (N + 1)

# 최솟값 구하는 점에서 오류 막고자
# 구하고자 하는 값 이외의 값은 0으로 셋팅
d[0] = 0

for i in range(1, N + 1):  # 카드 최대 개수까지 순환
    for k in range(1, i + 1):  # 여러 카드 팩 순환
        d[i] = min(d[i], d[i - k] + P[k])

print(d[N])
