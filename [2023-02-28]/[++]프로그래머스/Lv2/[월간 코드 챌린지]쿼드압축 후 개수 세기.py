def solution(arr):
    result = [0, 0]
    _len = len(arr)

    def logic(r, c, n):
        if n == 1:
            result[arr[r][c]] += 1
            return

        for i in range(r, r + n):
            for j in range(c, c + n):
                if arr[i][j] != arr[r][c]:
                    # 4방향 쪼개기
                    logic(r, c, n // 2)
                    logic(r + (n // 2), c, n // 2)
                    logic(r, c + (n // 2), n // 2)
                    logic(r + (n // 2), c + (n // 2), n // 2)
                    return

        result[arr[r][c]] += 1
        return

    logic(0, 0, _len)

    return result


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
