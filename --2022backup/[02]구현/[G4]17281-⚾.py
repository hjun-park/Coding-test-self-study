import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().rstrip())
results = [list(map(int, input().split())) for _ in range(N)]

'''
    참고: https://rhdtka21.tistory.com/89
'''

max_score = -1

for order in permutations((range(1, 9)), 8):
    # 1번 타자는 이미 4번 타순으로 등록되어 있기 때문에
    # 순열도 1~8만 구해주었고 4번 타순은 1번타자 (인덱스 0부터 시작하니 0으로 적음)로 등록
    order = list(order[:3]) + [0] + list(order[3:])
    start = 0  # 선발타자
    score = 0

    # i번째 이닝 ( 이닝마다 1-3루와 out_count 초기화 )
    for i in range(N):
        out_count = 0  # 아웃
        first, second, third = 0, 0, 0  # 1-3루

        while out_count < 3:  # 아웃이 될 때까지 진행
            result = results[i][order[start]]  # i번째 이닝의

            if result == 0:  # 아웃
                out_count += 1
            elif result == 1:  # 1루
                score += third
                first, second, third = 1, first, second
            elif result == 2:  # 2루
                score += (second + third)
                first, second, third = 0, 1, first
            elif result == 3:  # 3루
                score += (first + second + third)
                first, second, third = 0, 0, 1
            elif result == 4:  # 홈런
                score += (1 + first + second + third)
                first, second, third = 0, 0, 0

            start = (start + 1) % 9

    # max(max_score, score) 보다는 아래 식이 더 빠름
    if max_score < score:
        max_score = score

print(max_score)
