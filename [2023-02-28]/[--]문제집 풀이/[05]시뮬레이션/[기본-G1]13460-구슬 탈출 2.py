import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

'''
 1) .(빈칸) #(벽) O(구멍) R(빨간구슬) B(파란구슬)
 2) 구멍1개 구슬 각각 1개, 주변 벽
 3) 빨간 구슬 만을 꺼낸다, 파란 구슬은 X 동시에 빠져도 X
 4) 구슬이 서로 같은 칸에 있을 수 없다.
 5) 기울이는 건 구슬이 움직이지 않을 때까지 (혹은 10번 이상이라면 실패)
'''

# 1) 구슬의 위치 파악
# 2) 경로 찾기 ( BFS ) - visited에 두 구슬의 좌표를 담음 ( 4차원 배열 )
# 3) DFS 수행 ( title )

'''
 핵심: 만약 두 구슬이 만나면 움직임은 어떻게 ? 
  => 일단 구슬이 없다고 생각하고 움직인 후 가장 많이 움직인 것을 뒤로 미룬다.
  if next_rx == next_bx and next_ry == next_by:
    if r_count > b_count:
        next_rx -= dx[d]
        next_ry -= dy[d]
    else:
        next_bx -= dx[d]
        next_by -= dy[d]
'''

rx, ry, bx, by = [0] * 4

# 구슬의 위치를 파악한 후 q에 담음
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'B':
            bx, by = i, j
        elif graph[i][j] == 'R':
            rx, ry = i, j


# 기울이는 함수
def tilt(x, y, d):
    # 1) 다음 이동하는 곳이 벽이 아닌 경우
    # 2) 이동 후 내 위치가 구멍이 없는 경우만 이동
    count = 0
    while graph[x + dx[d]][y + dy[d]] != '#' and graph[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        count += 1  # 구슬의 이동거리

    # 3) 이동 하고났더니 다음이 벽이거나 자기 위치가 구멍인 경우 return
    return x, y, count


# 해당 방향으로 갈 수 있는지 검증
def can_move(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != '#':
        return True
    else:
        return False


# 기울일 수 있는 경로를 찾는 함수
def bfs():
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

    while q:
        qrx, qry, qbx, qby, depth = q.popleft()

        if depth > 10:
            print(-1)
            return

        for d in range(4):
            # if can_move(qrx, qry, d):
            nqrx, nqry, rcnt = tilt(qrx, qry, d)
            # if can_move(qbx, qby, d):
            nqbx, nqby, bcnt = tilt(qbx, qby, d)

            # 파란게 빠지면 다시 다른 로직 확인
            if graph[nqbx][nqby] == 'O':
                continue

            # 빨간게 빠지면 성공, 출력
            if graph[nqrx][nqry] == 'O':
                print(depth)
                return

            # 위 2개 중 아무것도 아니라면 공이 2개 만난 경우 조정
            if nqrx == nqbx and nqry == nqby:
                if rcnt > bcnt:
                    nqrx -= dx[d]
                    nqry -= dy[d]
                else:
                    nqbx -= dx[d]
                    nqby -= dy[d]

            # 다음 tilt 된 경우를 방문한 적이 없다면 추가로 진행
            if not visited[nqrx][nqry][nqbx][nqby]:
                visited[nqrx][nqry][nqbx][nqby] = True
                q.append((nqrx, nqry, nqbx, nqby, depth + 1))

    print(-1)  # 아무것도 아닌 경우 (공을 기울일 수 없는 경우


bfs()
