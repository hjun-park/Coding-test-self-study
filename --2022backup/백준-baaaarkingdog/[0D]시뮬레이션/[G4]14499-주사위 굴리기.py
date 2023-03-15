# import sys
#
# input = sys.stdin.readline
#
# N, M, x, y, K = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# orders = list(map(int, input().split()))
#
# # 동 서 북 남
# # 좌 우 상 하
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# '''
#     기본
#     [1, 2, 3, 4, 5, 6]
#     [4, 2, 1, 6, 5, 3]   # 동쪽
#     [3, 2, 6, 1, 5, 4]   # 서쪽
#     [2, 6, 3, 4, 1, 5]   # 남쪽
#     [5, 1, 3, 4, 6, 2]   # 북쪽
# '''
# # 주사위
# dices = [0] * 6
#
# # 1. 명령 개수만큼 이동
# for o in orders:
#     a, b, c, d, e, f = dices
#     nx = dx[o]
#     ny = dy[o]
#
#     if 0 <= nx < N and 0 <= ny < M:
#
#
#
#
#
