import sys

input = sys.stdin.readline

N, H = map(int, input().split())
down = [0] * (H + 1)
up = [0] * (H + 1)

'''
    참고: https://hongcoding.tistory.com/6
    1) 종유석, 석순을 나누어서 생각한다.
    2) 두 개를 합쳐서 조각의 개수를 세어 준다.
'''

# 석순의 경우 i 종유석의 경우 h-i+1
for i in range(N):
    if i % 2 == 0:  # 짝수의 경우 석순
        down[H - int(input().rstrip()) + 1] += 1
    else:   # 홀수의 경우 종유석
        up[int(input().rstrip())] += 1

# 각줄을 잘랐을 때 생기는 조각 개수를 구함
# 종유석 ( i+1 더 높은 데에는 무조건 종유석이 있음, 여러 번 더하기 때문에 누적합이 됨 )
for i in range(H-1, 0, -1):
    up[i] += up[i+1]

# 석순 (2부터 시작하는 이유는 종유석 1사이즈는 이미 세고 왔음)
# (i-1 더 낮은 데에는 무조건 석순이 있음, 여러 번 더하기 때문에 누적합이 됨)
for i in range(2, H+1):
    down[i] += down[i-1]

# 장애물의 총합을 구함
total = [0] * (H+1)
for i in range(1, H+1):
    total[i] = up[i] + down[i]

# 0번 인덱스 제외
res = total[1:]
v = min(res)
print(v, res.count(v))


