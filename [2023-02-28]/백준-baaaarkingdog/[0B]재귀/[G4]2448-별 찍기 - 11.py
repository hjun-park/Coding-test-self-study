import sys

input = sys.stdin.readline

N = int(input().rstrip())  # 높이
graph = [[' '] * 2 * N for _ in range(N)]


def func(n, x, y):
    # 3개일 때부터 출력 시작
    '''
      *         # 1라인
     * *        # 2라인
    *****       # 3라인
    '''
    if n == 3:
        graph[x][y] = '*'  # 1번째 라인
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'  # 2번째 라인
        for i in range(-2, 3):
            graph[x + 2][y - i] = '*'

    else:
        half = n >> 1
        func(half, x, y)  # 위(자기자신)
        func(half, x + half, y - half)  # 아래왼쪽
        func(half, x + half, y + half)  # 아래오른쪽


func(N, 0, N - 1)
for i in graph:
    print("".join(i))
