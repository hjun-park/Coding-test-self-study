def solution(rows, columns, queries):
    graph = [[y + columns * x for y in range(1, columns + 1)] for x in range(rows)]
    # for row in graph:
    #     print(*row)
    answer = []

    # graph = [[0] * columns for _ in range(rows)]
    # num = 1
    # answer = []
    # for i in range(rows):
    #     for j in range(columns):
    #         graph[i][j] = num
    #         num += 1



    for x1, y1, x2, y2 in queries:
        _min = int(1e9)  # 해당 턴에서의 최솟값
        before = graph[x1 - 1][y1 - 1]  # 초깃값 지정

        # x1, y1 다음 좌표부터 시작

        # 처음은 열이 증가하는 형태로 이동한다.
        for i in range(y1, y2):
            _min = min(_min, before)  # 이전값과 비교하여 최솟값 갱신
            before, graph[x1 - 1][i] = graph[x1 - 1][i], before  # 교체

        # 다음으로 행이 증가하는 형태로 이동한다.
        for i in range(x1, x2):
            _min = min(_min, before)
            before, graph[i][y2 - 1] = graph[i][y2 - 1], before

        # 다음으로 열 감소
        for i in range(y2 - 2, y1 - 2, -1):
            _min = min(_min, before)
            before, graph[x2 - 1][i] = graph[x2 - 1][i], before

        # 마지막 행 감소
        for i in range(x2 - 2, x1 - 2, -1):
            _min = min(_min, before)
            before, graph[i][y1 - 1] = graph[i][y1 - 1], before

        # 모두 거친 후 최소값 추가
        answer.append(_min)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
