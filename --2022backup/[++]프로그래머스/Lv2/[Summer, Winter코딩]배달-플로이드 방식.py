# 플로이드 워셜 알고리즘

INF = int(1e9)


def solution(N, road, K):
    # (1, N+1)

    # 1) 전부 INF로 초기화
    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    # 2) 자기자신은 0으로 초기화
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                graph[i][j] = 0

    # 3) road를 참고하여 초기화 (a, b, c)
    #  a <-> b 양방향 c로 초기화
    for r in road:
        a, b, c = r[0], r[1], r[2]
        if graph[a][b] < c:  # 예외처리
            continue
        graph[a][b] = c
        graph[b][a] = c

    # 4) k, i, j 돌면서 플로이드 워셜 만들기
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

    cnt = 0
    for i in graph[1]:
        if i <= K:
            cnt += 1
    return cnt


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
