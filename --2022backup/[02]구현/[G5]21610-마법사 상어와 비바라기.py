import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]

moves = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 구름의 처음 위치
cloud = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]

for d, s in info:
    is_disappear = [[False] * N for _ in range(N)]  # 사라진 구름 위치 정보

    # d 방향으로 s칸 이동한다.
    # for i in range(s):
    # 이동을 했는데 칸을 넘어간 경우는 어떻게 처리하지 ?
    # 구름 이동

    # print("========= 이동 전 클라우드 정보 =========")
    # print(cloud)

    # for j in range(4):
    for j in range(len(cloud)):
        cloud[j][0] += moves[d][0] * s
        cloud[j][0] %= N

        cloud[j][1] += moves[d][1] * s
        cloud[j][1] %= N

    # print("========= 이동한 클라우드 정보 =========")
    # print(cloud)

    # print("========= 비오기 전 =========")
    # for row in graph:
    # print(*row)

    # 구름에서 비가 내려 물의 양 증가
    for x, y in cloud:
        graph[x][y] += 1

    # print("========= 비온 후 =========")
    # for row in graph:
    # print(*row)

    # 물이 증가한 칸에 물복사버그 시전 ( 바구니의 수만큼 증가한다 )
    copy_moves = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    # for x, y in cloud:
    while cloud:
        x, y = cloud.pop()
        is_disappear[x][y] = True  # 사라진 위치 처리

        count = 0
        for cx, cy in copy_moves:
            nx = x + cx
            ny = y + cy

            # 경계를 넘어가는 칸은 인접한 대각선 칸이 아니다.
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 0:
                    count += 1

        graph[x][y] += count

    # print("========= 물복사 버그 이후 =========")
    # for row in graph:
    # print(*row)

    # 바구니에 저장된 물이 2이상이면 칸 구름 생긴 후 물의 양 2 감소
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and not is_disappear[i][j]:
                graph[i][j] -= 2
                cloud.append([i, j])

print(sum(map(sum, graph)))
