def solution(m, n, board):
    x2 = []

    # 리스트 처리
    for row in board:
        x2.append(list(row))

    is_crash = True
    while is_crash:
        start = []
        is_crash = False

        # [터질만한 곳 모두 리스트 담기]
        for i in range(m - 1):
            for j in range(n - 1):
                if x2[i][j] == x2[i][j + 1] == x2[i + 1][j] == x2[i + 1][j + 1] != '.':
                    start.append([i, j])
                    is_crash = True

        # [터지는 동작 한 번에 처리]
        for i2 in start:
            i, j = i2[0], i2[1]
            x2[i][j], x2[i][j + 1], x2[i + 1][j], x2[i + 1][j + 1] = '.', '.', '.', '.'

        # [블록이 중력을 받아 down 되는 동작]
        for _ in range(m):
            for i in range(m - 1):  # 첫 번재 행부터 마지막-1번째 행 전까지 진행
                for j in range(n):
                    if x2[i + 1][j] == '.':  # 다음 행이 .이라면 서로 교체
                        x2[i + 1][j], x2[i][j] = x2[i][j], '.'

    cnt = 0
    for i in x2:
        cnt += i.count('.')
    return cnt


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
