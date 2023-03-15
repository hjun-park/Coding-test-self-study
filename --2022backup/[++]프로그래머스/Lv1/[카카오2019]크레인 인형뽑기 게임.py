def solution(board, moves):
    basket = []
    answer = 0

    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                basket.append(board[i][m - 1])
                board[i][m - 1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        answer += 2
                break
    return answer

# print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
#                [1, 5, 3, 5, 1, 2, 1, 4]))

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [1, 2, 3, 4, 5]))
