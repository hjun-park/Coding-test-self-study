import sys
from collections import deque

input = sys.stdin.readline

# 데스나이트 이동 방향
moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False] * N for _ in range(N)]


# 이동 할 수 X 경우 -> -1

def bfs(x, y):
    min_count = 1e9
    q = deque()
    q.append((x, y, 0))

    while q:
        # 체크
        r, c, count = q.popleft()
        if r == r2 and c == c2:
            min_count = min(min_count, count)

        # 1) 범위를 벗어난 경우 제외
        # 문제점: 무한루프 돌 가능성 있음 ( visited 체크 안 함 )
        for m in moves:
            nr = r + m[0]
            nc = c + m[1]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, count + 1))

    if min_count == 1e9:
        return -1
    else:
        return min_count


print(bfs(r1, c1))
