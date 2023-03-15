def solution(n, arr1, arr2):
    _len = len(bin(2 ** n - 1)[2:])
    graph = [['#' for _ in range(n)] for _ in range(n)]
    result = []

    for i in range(n):
        a = bin(arr1[i])[2:].zfill(_len)
        b = bin(arr2[i])[2:].zfill(_len)

        # a와 b의 문자를 비교해서 둘 다 0이라면 graph를 공백으로 변경
        for j in range(len(a)):
            if a[j] == '0' and b[j] == '0':
                graph[i][j] = ' '

    for row in graph:
        result.append(''.join(row))

    return result


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
