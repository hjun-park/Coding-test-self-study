# BFS 문제 핵심 정리

- - -

**기입할 점**

1) 어떻게 어떤 생각으로 문제를 접근하여 어떤 아이디어를 냈는가 ?
2) 특별히 어느 부분이 구현이 힘들었고 그건 어떻게 구현을 하였는가 ?
3) 나는 어떤 부분이 어려웠고 무엇을 배웠는가 ?

- - -

## [G5]4179-불!

1) 어떻게 어떤 생각으로 문제를 접근하여 어떤 아이디어를 냈는가

- 처음에는 지훈이가 이동 후 불이 이동하니, deepcopy 처리하려고 했다.
- 그리고 지훈이가 이동하는 부분은 bfs로 처리하고 불은 완전탐색으로 하려고했다.

2) 특별히 어느 부분이 구현이 힘들었고 그건 어떻게 구현을 하였는가 ?

- 그중에서도 불을 이동하고 지훈이가 이동할 때 시간체크를 하는 것이 문제였다.
- 굳이 deepcopy를 쓸 필요가 없었다.

3) 나는 어떤 부분이 어려웠고 무엇을 배웠는가 ?

- deepcopy 대신에 지훈이도 deque 만들어 bfs 순환, 불도 deque 만들어 bfs 순환해주면 되었다.
- visited에 시간을 체크하는 방법 뿐만 아니라 문자가 들어 있는 graph에도 시간을 체크하는 방법이 있다.
- 자세한 것은 아래 코드를 참고한다.

```python

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


```

<br >

- - -

## [G3]9466-텀 프로젝트

[참고1](https://par3k.tistory.com/16)

[참고2](https://deep-learning-study.tistory.com/583)

1) 어떻게 어떤 생각으로 문제를 접근하여 어떤 아이디어를 냈는가 ?
    - 사이클을 찾아야 했다. 그래서 BFS를 이용하여 체크하려고 했다.
2) 특별히 어느 부분이 구현이 힘들었고 그건 어떻게 구현을 하였는가 ?
    - 사이클을 찾긴 찾아야겠는데 어떻게 찾아야할 지 모르겠다.
    - BFS가 아닌 DFS로 그리고 계속해서 방문하면서 방문지역은 traced에 기록하였다. 계속 방문할 때 처음으로 방문했던 곳을 또 방문하면서 traced에 있는 것을 만나면 싸이클의 시작이라는 점.
3) 나는 어떤 부분이 어려웠고 무엇을 배웠는가 ?
    - BFS, 그리고 사이클을 찾는 방법. (계속 기록 & 방문처리 하면서 돌다가 기록했던게 또 나온다면 그게 시작점 )

### 문제 요약

1) 팀원 수 제한 X, 1개 팀만, 그리고 1인 팀도 가능하다.
2) 모든 학생은 같이 플젝할 1명만 선택한다.
3) 혼자 하려면 자기 자신을 선택한다.
4) 자기 자신을 가리키거나 혹은 사이클을 형성해야만 팀이 될 수 있다.
5) 구하려는 것 : 팀에 속하지 않는 학생 수

### 문제의 핵심

1) 사이클은 DFS를 이용하여 순환되는 graph를 찾을 수 있다.
2) 마지막 node와 첫 node가 이어져서 Loop를 이루는 것을 찾는다.

```python
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(v):
    global team_students

    # 3) 시작지는 방문처리 및 탐색 중인 경로 추가
    visited[v] = True
    traced.append(v)

    # 4) 다음 방문할 정점을 설정한다. (시작지를 graph 인덱스로 집어넣으면 됨)
    next = graph[v]

    # 5) 방문할 정점이 방문된 상태이면서 traced에 있다면 거기서부터 사이클이 시작된다는 것이다.
    if visited[next]:
        if next in traced:  # 사이클이 시작되는 구간부터 팀을 이룬다.
            team_students += traced[traced.index(next):]
        return  # 아닌 경우라면 모든 곳을 방문했으므로 return
    # 6) 다음 정점이 방문된 상태가 아니라면 다시 dfs를 순회한다.
    else:
        dfs(next)


for _ in range(int(input().rstrip())):
    # 1) 기본적인 정보 생성
    N = int(input().rstrip())

    # 문제에서 index가 1부터 시작하므로 앞에 0을 붙여주거나 개수를 1개 더 추가해주면 편리하다.
    graph = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N
    team_students = []

    for i in range(1, N + 1):
        # 2) 방문하지 않은 경우만 탐색한다.
        if not visited[i]:
            traced = []
            dfs(i)

    # 7) 그렇게 하면 팀으로 구성된 학생들이 나오고 전체 학생 수에서 해당 학생 수를 빼주면 된다.
    print(N - len(team_students))


```

<br >

- - -

## [G3]2146-다리 만들기

1) 어떻게 어떤 생각으로 문제를 접근하여 어떤 아이디어를 냈는가

- BFS를 이용하여 섬의 번호를 인덱싱한다.
- 그다음 각 섬마다 BFS를 이용하여 거리를 체크한다.

2) 특별히 어느 부분이 구현이 힘들었고 그건 어떻게 구현을 하였는가 ?

- 2번 BFS를 사용한다는 아이디어는 냈지만 거리체크하는게 어려웠다.
- 1부터 섬의 개수까지 for문으로 돌리면서 처음에는 완전탐색으로 탐색할 섬의 거리를 0으로 만든다. (해당 섬은 모두 거리 0이니까)
- 방문하지 않은 섬은 -1로 표기하였고 바다를 만나면 +1씩 계산하면 된다.
- 이는 shortest_bfs2에서 자세히 구현되어 있다.

3) 나는 어떤 부분이 어려웠고 무엇을 배웠는가 ?

- 구현파트

```python
import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def find_bfs(start_x, start_y, index):
    global visited

    q = deque()
    visited[start_x][start_y] = True
    graph[start_x][start_y] = index
    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = index


def shortest_bfs2(num):
    # 2-1) 거리를 기록할 visited와 min_dist 선언
    visited = [[-1] * N for _ in range(N)]
    q = deque()

    # 2-2) graph 전체를 순회하면서 num인 부분은 queue에 집어넣어주고 거리 0으로 초기화
    # -> 특정 num을 가진 섬은 전체 한번씩 확인할 예정, 따라서 거리 0으로 초기화
    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                visited[i][j] = 0
                q.append((i, j))

    # 2-3) 큐를 돌며 BFS 시작
    #   - 0이 아니고 다른 섬 번호를 만나면 해당 visited 값에 거리를 새로 갱신하고 최솟값은 min_dist에 할당
    #   - 만약 0이고(바다) 거리도 -1이라면(미방문 상태) q에 넣어주고 visited +1 처리
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                # 2-4) graph[nx][ny] != num이라면 가장 먼저 다른 섬을 먼저 만난 것이므로 거리 return
                if graph[nx][ny] != num and graph[nx][ny] != 0:
                    return visited[x][y]

                # 2-5) 방문하지 않았으면서 바다인 경우에만 q에 집어넣고 거리 방문처리
                if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


# 1) 섬에 index 번호 주기
visited = [[False] * N for _ in range(N)]
index = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and not visited[i][j]:
            index += 1
            find_bfs(i, j, index)

# 2) 섬과 섬끼리 가장 가까운 거리 구하기
cnt = index  # 섬의 개수
answer = int(1e9)
for i in range(1, cnt + 1):
    answer = min(answer, shortest_bfs2(i))

print(answer)


```

<br >

- - -

## [G4]1600-말이 되고픈 원숭이

1) 어떻게 어떤 생각으로 문제를 접근하여 어떤 아이디어를 냈는가 ?

- 원숭이를 말처럼 K번 이동 시킨 후 4방향 이동시키자.
- 경로를 찾기 위해서 BFS 이용

2) 특별히 어느 부분이 구현이 힘들었고 그건 어떻게 구현을 하였는가 ?

- 맞왜틀 문제였다. 제시된 TestCase는 다 통과하지만 통과 못하는 Case가 있었다.

3) 나는 어떤 부분이 어려웠고 무엇을 배웠는가 ?

- 말처럼 대각선으로 이동하는 것과 4방향 인접이동 하는 것을 분리해야 했는데 처음에는 코드를 중복작성해서 하려고 했다.
- 하지만 그렇게 하지 않고도 2차원이었던 visited를 3차원으로 만들어 대각선 말 이동과 4방향 인접이동으로 분리 가능했다.

```python
import sys
from collections import deque

input = sys.stdin.readline

moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 원숭이는 K번만 말처럼 이동 가능, 그 이후는 인접한 칸으로만 이동 가능

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0 for _ in range(31)] for _ in range(W)] for _ in range(H)]

    while q:
        x, y, cnt = q.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][cnt]

        '''
         내가 한 실수:
          - 이렇게 하면 대각선 먼저, 이후 상하좌우가 돌게 된다. (visited를 대각선 먼저 체크하니까)
          - [1] 대각선과 상하좌우 도는걸 분리하자.
          
          - [1] 그럼 어떻게 분리할건데? => 차원을 늘려준다. 기존 2차원에서 3차원으로.
          - visited를 3차원 배열로 만들었다. x는 Height, y는 Width, cnt는 z축으로 원숭이가 말처럼 몇 번 이동했는지 체크
          - 이렇게 해서 원숭이가 인접향 4방향을 먼저 돌고 그 다음에는 말처럼 이동했다는 의미로 cnt + 1 해서 대각선(말 이동방향) 이동한다.
          [참고](https://pacific-ocean.tistory.com/393)
        '''

        # 1) 4방향 이동 먼저
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < H and 0 <= ny < W:
                if visited[nx][ny][cnt] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cnt))

        # 2) 대각선(말의 방향) 대로 이동 가능한 경우
        if cnt < K:
            for m in moves:
                nx = x + m[0]
                ny = y + m[1]

                if 0 <= nx < H and 0 <= ny < W:
                    if visited[nx][ny][cnt + 1] == 0 and graph[nx][ny] == 0:
                        visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                        q.append((nx, ny, cnt + 1))

    return -1


K = int(input().rstrip())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

print(bfs())

```
