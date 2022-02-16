import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

R, C = map(int, input().split())
graph = []

# 불의 방문처리 ( 1이 방문된 상태 )
visited = [[0] * C for _ in range(R)]
f = deque()
q = deque()

''' 
 1) 좌표 표시
  - 처음 지훈 위치 : J
  - 불의 위치 : F
  - 지훈이가 이동할 때 위치 : 정수값 (몇 분)
  - 벽 : #
  - 이동가능 : .
  
  2) visited를 2개 만들어서 불과 지훈이의 이동경로를 처리하기에는 메모리가 부족하다.
     따라서 불의 이동 경로만 visited를 만들어주고 
     시간체크만 해도 되는 지훈이는, 지훈이 이동 경로에는 몇 분이 걸렸나 graph에 체크한다.
'''


def bfs():
    # 2) 지훈이와 불이 이동하는 두 deque
    global q, f

    # 2) 무한루프
    while True:
        # 2-1) 지훈이가 이동할 수 있는 곳은 따로 담아둔다.
        #      그 이유는 지훈이의 이동 + 불의 이동이 1초라서 그렇다.
        temp = deque()
        while q:
            x, y = q.popleft()

            # 2-2) q에서 꺼낸 위치가 미로의 가장자리면서 현재 위치에 불이 없다면 탈출 가능
            if (x == R - 1 or y == C - 1 or x == 0 or y == 0) and graph[x][y] != 'F':
                return graph[x][y] + 1  # 지훈 위치 (시간) 반환

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # 2-3) 범위 내에서 다음 이동할 위치가 '.' 이면서 현재 위치에 불이 없다면 시간체크 & 이동
                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == '.' and graph[x][y] != 'F':
                        graph[nx][ny] = graph[x][y] + 1
                        temp.append((nx, ny))

        # 3) 지훈이가 1초동안 이동 가능한 곳은 temp이고 이동이 끝났으므로 q에 다시 담아둔다.
        q = temp

        # 4) 큐가 비어 있으면 불 혹은 장애물로 둘러싸인 상태이므로 이동 불가
        if not q:
            return "IMPOSSIBLE"

        # 5) 다음으로 지훈이가 아닌 불이 1초동안 이동할 수 있는 곳을 파악하기 위해 temp를 초기화한다.
        temp = deque()
        while f:
            x, y = f.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # 6) 이동하려는 곳이 이동 범위 이내이며, 벽이 아니면서 방문하지 않았다면
                #    temp에 위치를 담아두고 방문처리 후 해당 위치를 불태운다.
                if 0 <= nx < R and 0 <= ny < C:
                    if not visited[nx][ny] and graph[nx][ny] != "#":
                        temp.append([nx, ny])
                        visited[nx][ny] = True
                        graph[nx][ny] = "F"

        # 7) 불이 1초동안 이동 가능한 곳은 temp이고 이동이 끝났으므로 다시 f 담아둔다.
        f = temp


# 1) 가장 먼저 지훈 위치와 불의 위치를 deque에 담아준다.
#    graph에는 장애물과 불 위치가 문자로 주어져 있지만
#    지훈이가 있는 곳 (J)는 시간을 세기 위해 정수 0으로 초기화한다.
#    앞으로 지훈이가 이동하는 경로는 몇 분에 위치해 있는지 시간 값으로 덮어 쓸 것이다.
#    visited를 이용해서 시간초를 체크하면 좋겠지만,
#    이렇게하는 이유는 문제에서 주어진 메모리가 한정되어 있기 때문이다.
def find():
    for i in range(R):
        a = list(input().rstrip())
        graph.append(a)
        for j in range(C):
            if a[j] == 'J':
                q.append((i, j))
                graph[i][j] = 0  # 다른데는 문자이지만 지훈이의 위치로 시간을 셀 예정
            elif a[j] == 'F':
                f.append((i, j))
                visited[i][j] = True


find()
print(bfs())
