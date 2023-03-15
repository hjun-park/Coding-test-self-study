import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 입력으로 주어지는 사무실의 모양
graph1 = [list(map(int, input().split())) for _ in range(N)]

# CCTV 방향 정한 후 CCTV 감시 영역에 걸리는 칸을 7로 마킹할 모양
graph2 = [[0] * M for _ in range(N)]

# cctv 좌표를 담을 변수
cctv = []

# 반시계방향
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# (x, y)에서 dir방향 진행하며 벽을 만날 때까지 지나가는 모든 빈 칸을 7로 변경함
def upd(x, y, dir):
    dir %= 4
    dir = int(dir)
    # 내가 기존에 했던 BFS 방식과 다르게 쭉 진행해야 하는 경우는 while True 사용
    while True:
        x += dx[dir]
        y += dy[dir]

        if (not 0 <= x < N or not 0 <= y < M) or graph2[x][y] == 6:  # 범위 안에 없거나 벽이 있다면
            return

        if graph2[x][y] != 0:  # CCTV가 있는 자리라면 continue
            continue

        graph2[x][y] = 7  # 지나가는 길 마킹


# ===================================
# 0. CCTV 추가
# ===================================
empty = 0
for i in range(N):
    for j in range(M):
        if graph1[i][j] != 0 and graph1[i][j] != 6:  # CCTV 라면
            cctv.append((i, j))
        if graph1[i][j] == 0:  # 빈 칸이라면
            empty += 1  # CCTV가 아예 없는 것도 고려해야하니, 빈칸의 개수로 맞추는게 안전

# ========================================
# 1. CCTV 방향 지정 (4진법 사용, 백트래킹보다 효율적)
# =======================================
for tmp in range(0, 1 << (2 * len(cctv))):  # CCTV 개수만큼 loop를 돈다.
    for i in range(0, N):
        for j in range(0, M):
            graph2[i][j] = graph1[i][j]  # upd 함수를 거치며 graph2가 변경됨
    brute = tmp
    for i in range(0, len(cctv)):
        dir = brute % 4
        brute /= 4

        x = cctv[i][0]
        y = cctv[i][1]

        # 1번 CCTV는 한 방향으로 upd 진행
        if graph1[x][y] == 1:
            upd(x, y, dir)

        # 2번 CCTV는 서로 마주보는 방향으로 진행
        elif graph1[x][y] == 2:
            upd(x, y, dir)
            upd(x, y, dir + 2)

        # 3번 CCTV는 직각이므로 dir, dir+1
        elif graph1[x][y] == 3:
            upd(x, y, dir)
            upd(x, y, dir + 1)

        # 4번 cctv는 세 방향
        elif graph1[x][y] == 4:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)

        # 5번 cctv는 네 방향
        else:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
            upd(x, y, dir + 3)

        # ========================================
        # 2. 각 CCTV마다 가면서 마킹을 남기고 마킹이 없는 부분을 센다.
        # =======================================
        val = 0
        for i in range(N):
            for j in range(M):
                val += 1 if graph2[i][j] == 0 else 0
        empty = min(empty, val) # 가장 최솟값으로 갱신

print(empty)
