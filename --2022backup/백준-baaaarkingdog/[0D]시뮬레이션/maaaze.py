import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

'''
    1. [판을 쌓는다] 순열을 사용하여 판을 쌓는다. (판을 쌓은 후 판 전체를 복사) 
    2. [판을 회전한다] 회전은 4번 가능, 재귀 사용하여 처음과 끝부분에 도달 가능해야만 다음 로직 가능  
        함수정의 : def logic(layer) (해당 계층에서 회전할 지 말지를 정하는 재귀식)
        base condition :  layer가 5일 때 검증하고 탈출구가 있으면 다음 수행 아니면 그냥 return
    3. [탈출구가 있는지 확인한다] bfs 순환
 
'''

# 시뮬레이션 브루트포스 BFS
# deque 사용
graph = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]

times = []

# 위 좌 상 우 하 아래 시계 방향
dx = [0, 0, -1, 0, 1, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [1, 0, 0, 0, 0, -1]


# 하양 : o (1)
# 검은 : x (0)
# 탈출 불가능 -1

# 판 시계 반시계
def tilt(layer):
    temp = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            # 음수가 나올 수 있기 때문에  5 - 1 - i가 온다.
            temp[j][4 - i] = maze[layer][i][j]

    maze[layer] = temp  # 이후 maze가 바로 사용되기 때문에 deepcopy까지 할 필요 없음
    '''
       (2,0) -> (0, 2)
       (2,2) -> (2, 2)
       (4,2) -> (2, 0)
       (2,1) -> (1, 2)

       (0,2) -> (2,5)
       (2,0) -> (0,2)
       // x, y 좌표 바꿔주고 4-j


    '''


# 미로판 순회
def bfs():
    # 1. 미로 이동경로를 담을 queue를 생성하고 최초 시작지를 담는다.
    q = deque()
    q.append((0, 0, 0))

    # 2. 방문여부를 담을 리스트를 선언하고 최초 시작지는 초기화 한다.
    #    방문여부에는 해당 지점까지의 최소거리가 담긴다.
    visited = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0

    # 3. 이동경로를 하나하나 순회 시작한다.
    while q:
        # 1. 맨 처음 경로를 꺼낸다.
        z, x, y = q.popleft()

        # 2. 맨 끝에 도달했다면 시간 배열에 값을 담는다.
        #    도착지를 찾았다면 더 이상 수행할 로직이 없으므로 빠져나온다.
        if x == 4 and y == 4 and z == 4:
            times.append(visited[z][x][y])
            return

        # 3. 위 아래, 좌상우하
        for d in range(6):
            # 1. 다음 이동지를 정의
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            # 2. 범위에 있으면서,
            if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                # 3. 방문하지 않았고 미로위치도 갈 수 있는 위치라면
                if visited[nz][nx][ny] == -1 and maze[nz][nx][ny] != 0:
                    visited[nz][nx][ny] = visited[z][x][y] + 1  # 이동횟수 대입
                    q.append((nz, nx, ny))      # 다음 이동경로 추가


def check_recursion(layer):
    # base condition //맨 마지막 층일 때
    if layer == 5:
        if maze[4][4][4]:   # 탈출구가 있다면 bfs 수행
            bfs()
        return

    for _ in range(4):  # 회전은 4번까지 가능
        if maze[0][0][0]:   # 출발지가 있는 경우에만 다음 층 검증
            check_recursion(layer + 1)
        tilt(layer) # 없을 경우 혹은 검증 후에는 회전


# 1. [판을 쌓는다] 순열을 사용하여 판을 쌓는다. (판을 쌓은 후 판 전체를 복사)
# for p in permutations([x for x in range(5)]):
#     for i in p:
#         maze[i] = graph[i]

for p in permutations([0, 1, 2, 3, 4]):
    for i in range(5):
        maze[p[i]] = graph[i]

    check_recursion(0)

print(min(times) if times else -1)
