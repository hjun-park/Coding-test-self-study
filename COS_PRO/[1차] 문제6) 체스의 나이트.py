def solution(pos):
    move_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    answer = 0

    # 입력 처리
    x = move_dict[pos[0]]
    y = int(pos[1]) - 1

    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
    board = [[0] * 8 for _ in range(8)]

    for m in moves:
        nx = x + m[0]
        ny = y + m[1]

        if 0 <= nx < 8 and 0 <= ny < 8:
            answer += 1

    return answer


pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")
