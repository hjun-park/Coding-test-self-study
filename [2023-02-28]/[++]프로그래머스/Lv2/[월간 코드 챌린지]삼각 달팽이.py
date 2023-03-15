from itertools import chain

# 아래 / 우측 / 좌상단(위)
dx = [1, 0, -1]
dy = [0, 1, -1]


def solution(n):
    answer = []
    # 삼각형 구조
    graph = [[0] * (i + 1) for i in range(n)]

    x, y = -1, 0
    num = 1
    for i in range(n):  # 회전 횟수
        d = i % 3
        for j in range(i, n):  # 나아갈 컬럼 갯수
            x += dx[d]
            y += dy[d]

            graph[x][y] = num
            num += 1

    return list(chain(*graph))
