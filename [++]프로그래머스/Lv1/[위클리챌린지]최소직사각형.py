def solution(sizes):
    # 왼쪽에 큰 값이 오게 함
    for size in sizes:
        if size[1] > size[0]:
            size[0], size[1] = size[1], size[0]

    l, r = -1, -1

    for size in sizes:
        l = max(size[0], l)
        r = max(size[1], r)

    return l * r


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
