from itertools import chain  # 2차원배열을 1차원으로 잇거나 여러 리스트들을 이어줌


# DP 문제 ( (i,j)의 값은 min(좌, 상, 좌상) + 1 이다. )
def solution(board):
    N, M = len(board), len(board[0])

    for x in range(1, N):
        for y in range(1, M):
            if board[x][y] == 1:
                board[x][y] = min(board[x - 1][y], board[x][y - 1], board[x - 1][y - 1]) + 1

    return max(chain(*board)) ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1], [1, 1, 1, 1]]))
