import heapq
import sys

input = sys.stdin.readline

# 1) 낚시왕이 이동하여 잡는 경우
# 2) 상어가 이동하는 경우 ( 이동 후에는 상어끼리 잡아먹음 )

'''
    https://developer-ellen.tistory.com/60?category=879172
    
    1. graph에 상어의 정보를 입력받아 저장
     - 그래프를 3차원배열로 만들어 마지막 z축에는 (사이즈, 속력, 방향)을 집어넣는다.

    2. 낚시왕이 한 칸 열을 뒤로 이동하고 그래프를 돌면서 특정 열에 대한 생선을 잡는다.
     - 생선을 잡는 순간 break

    3. 특정 열에 대한 생선을 잡은 후에는 상어의 이동이 이루어진다.
     - 3-0) 상어의 위치를 저장할 비어있는 R*C*list() 3차원 g 배열 생성
     - 3-1) for문을 돌리면서 x, y 좌표가 비어있지 않으면 현위치의 상어 (사이즈, 속력, 방향) 정보를 빼온다.
     - 3-2) 속력을 백업하고 백업한 속력값을 가지고 while문을 돌린다. [실질적 상어 이동]
       > 이동이 불가능하면 방향을 바꾸어준다.
       > 이동이 가능하면 이동 후에 while문 탈출을 위한 백업한 속력값을 감소시킨다.
     - 3-3) while문이 끝나게 되면 상어의 이동이 다 끝난 것이다. g 배열에 (사이즈, 속력, 방향) 저장한다.
       > 굳이 g배열 만들어서 쓰는 이유는, 중복 이동이 발생하면 안 되기 때문에 만들어서 씀
       > 혹여나 이동했는데 같아질 수 있는 걱정이 있겠지만 append를 하기 때문에 추가가 되지, 중복되지는 않음
     - 3-4) for문이 다 끝나게 되면 graph값을 g값으로 복사해서 붙여넣는 작업을 한다.

    4. 좌표당 상어 2마리 이상인 경우 가장 큰 사이즈만 남게 한다.
      - for문으로 순회하면서 크기가 2이상인 경우에 대해서 size를 대상으로 역순정렬 후
      - size만큼 while문을 돌리면서 하나씩 뺀다.

'''

R, C, M = map(int, input().split())
graph = [[list() for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    heapq.heappush(graph[r - 1][c - 1], (z, s, d))

king = -1
weight = 0

# 상 하 우 좌
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4


def move_king():
    global king, weight

    king += 1

    for i in range(R):
        if graph[i][king]:
            weight += heapq.heappop(graph[i][king])[0]
            break


def move_shark_v2():
    g = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j
                size, speed, d = heapq.heappop(graph[i][j])
                s_count = speed  # 속도만큼 이동
                while s_count > 0:
                    # 이전에 내가 시도한 방식은 nx = x + dx[d] * s_count 였는데,
                    # 방향 틀기가 매우 어려웠다. 한 칸씩 이동하는 것도 괜찮은 방법인 듯
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 한 칸 이동했는데 범위를 벗어난 경우 방향 전환
                    if 0 > nx or nx >= R or ny < 0 or ny >= C:
                        if d in [UP, RIGHT]:
                            d += 1
                        elif d in [DOWN, LEFT]:
                            d -= 1
                        continue
                    # 이동이 가능한 경우 직접 이동해준 후에 이동 count 제거
                    else:
                        x, y = nx, ny
                        s_count -= 1

                # 이동을 완료하면 해당 위치에 상어 집어넣기
                # heapq.heappush(graph[x][y], (size, speed, d))
                g[x][y].append([size, speed, d])

    # 2마리 이상 상어가 있을 경우 잡아먹는다.
    for i in range(R):
        for j in range(C):
            graph[i][j] = g[i][j]

    # 오류났던 문장
    # for i in range(R):
    #     for j in range(C):
    #         while len(graph[i][j]) > 1:
    #             heapq.heappop(graph[i][j])


while True:
    move_king()
    move_shark_v2()

    if king == C - 1:
        break

print(weight)
