import sys

input = sys.stdin.readline

'''
 - 매 초마다 2개 나무 중 하나에서 열매 떨어지고 그 위치에 자두가 있으면 먹을 수 있음
 - T초마다 떨어질 때 자두는 최대 W까지만 이동하려고 함
 - 참고 url: https://www.crocus.co.kr/758
'''

T, W = map(int, input().split())

# 최대개수[시간][위치][이동횟수]
d = [[[0] * 32 for _ in range(3)] for _ in range(1002)]

# 자두[시간][위치]
plums = [[0] * 3 for _ in range(1002)]

for i in range(1, T+1):
    pos = int(input().rstrip())
    plums[i][pos] = 1

# 1초값은 초기화
d[1][1][0] = plums[1][1]
d[1][2][1] = plums[1][2]

# 점화식 이용, 채워주기
_max = max(d[1][1][0], d[1][2][1])  # max값 주의하기
for t in range(2, T + 1):
    for m in range(0, W + 1):
        # t-1초에서 t초로 갔다. 이동이 2에서 1로 갔다면 이동횟수는 m-1에서 m이다. + 현재 자두
        d[t][1][m] = max(d[t - 1][1][m], d[t - 1][2][m - 1]) + plums[t][1]
        d[t][2][m] = max(d[t - 1][2][m], d[t - 1][1][m - 1]) + plums[t][2]

        # 최댓값 갱신
        _max = max(_max, d[t][1][m])
        _max = max(_max, d[t][2][m])

print(_max)
