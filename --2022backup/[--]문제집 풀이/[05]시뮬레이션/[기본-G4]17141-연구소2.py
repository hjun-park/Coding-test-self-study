import sys
from collections import deque

'''
1. 바이러스를 놓을 수 있는 좌표를 virus에 저장하고 지도에는 0으로 입력
2. dfs로 조합을 구현하여 바이러스 m개를 고르고 bfs로 이동
3. bfs에서는 이동 횟수의 최대값을 cnt에 기록한다
4. 탐색을 마치고 빈 칸인데 방문하지 않았으면 cnt를 정수 최대값으로 설정
5. 최소 시간을 ans에 저장하고 모든 경우를 탐색한 후 출력 
'''

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 3. bfs에서는 이동 횟수의 최대값을 cnt에 기록한다
def bfs():
    global q, visited, ans
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if a[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append([nx, ny])

    # 4. 탐색을 마치고 빈 칸인데 방문하지 않았으면 cnt를 정수 최대값으로 설정
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0 and visited[i][j] == -1:
                cnt = sys.maxsize
    # 5. 최소 시간을 ans에 저장하고 모든 경우를 탐색한 후 출력
    ans = min(ans, cnt)


def dfs(index, cnt):
    global q, visited, ans
    if cnt == m:
        q = deque()
        visited = [[-1] * n for _ in range(n)]
        for i in range(len(virus)):
            if select[i]:
                q.append([virus[i][0], virus[i][1]])
                visited[virus[i][0]][virus[i][1]] = 0
        bfs()
        return

    # 2. dfs로 조합을 구현하여 바이러스 m개를 고르고 bfs로 이동
    for i in range(index, len(virus)):
        if select[i]:
            continue
        select[i] = 1
        dfs(i + 1, cnt + 1)
        select[i] = 0


n, m = map(int, input().split())

# 1) 바이러스는 따로 저장하고 기존 지도의 2는 0으로 변경
a, virus = [], []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for j in range(n):
        if a[i][j] == 2:
            virus.append([i, j])
            a[i][j] = 0

select = [0 for _ in range(10)]
ans = sys.maxsize
dfs(0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
