def get_pos(line):
    pos = []
    for i in range(len(line)):
        a, b, e = line[i]

        for c, d, f in line[i + 1:]:
            if a * d - b * c == 0:
                continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if int(x) == x and int(y) == y and (x, y) not in pos:
                pos.append((int(x), int(y)))

    return pos


def solution(line):
    _max, _min = -1, int(1e9)

    pos = get_pos(line)

    s1 = sorted(pos, key=lambda x: x[0])
    s2 = sorted(pos, key=lambda x: x[1])

    # X좌표에서의 최소 최대
    min_n = s1[0][0]
    max_n = s1[-1][0]

    # Y좌표에서의 최소 최대
    min_m = s2[0][1]
    max_m = s2[-1][1]

    # 행열에서의 (0, 1)이 좌표에서는 (1, 0)이다.
    N = max_m - min_m + 1
    M = max_n - min_n + 1

    graph = [['.' for _ in range(M)] for _ in range(N)]

    for x, y in pos:
        # min_을 사용한 이유는 graph에서 0값으로 보정하기 위함이며
        # 마찬가지로 행열에서의 (0,1)이 좌표에서는 (1,0)이니까 r, c는 반대로 집어넣는다.
        r, c = y - min_m, x - min_n
        graph[r][c] = "*"

    # 배열과 좌표는 행과 열이 증가하는 방향이 반대이다. 그래서 뒤집는다.
    # join 사용
    return [''.join(x) for x in graph][::-1]


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
