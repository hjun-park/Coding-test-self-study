import random
import sys

input = sys.stdin.readline

'''
 지뢰 : -1
 지뢰가 count 되지 않고 지뢰가 없는 경우 : 0  (초깃값)
 지뢰가 아니지만 count된 수 : 양수
'''

# 1) 그래프 초기화
graph = [[0] * 10 for _ in range(10)]


# 3) 지뢰 주변 카운트 증가
def count_near_mine(x, y):
    moves = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    for m in moves:
        nx = x + m[0]
        ny = y + m[1]

        if 0 <= nx < 10 and 0 <= ny < 10:
            if graph[nx][ny] != -1:  # 지뢰가 없다면
                graph[nx][ny] += 1  # 지뢰 수 count


# 2) 지뢰 설치
def set_mine():
    # random.sample(range(1, 11), 10)
    count = 0  # 지뢰 설치 개수

    while count < 10:
        rand_x = random.randrange(0, 10)
        rand_y = random.randrange(0, 10)

        # 지뢰를 설치하는 경우
        if graph[rand_x][rand_y] != -1:
            count += 1
            graph[rand_x][rand_y] = -1
            count_near_mine(rand_x, rand_y)


set_mine()
for row in graph:
    print(*row)
