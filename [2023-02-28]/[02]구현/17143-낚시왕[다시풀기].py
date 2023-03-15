import sys

'''
    백준에 제출하면 typeError만 계속 표시됨
'''
'''
    1. graph에 상어의 정보를 입력받아 저장
     - 그래프를 3차원배열로 만들어 마지막 z축에는 (사이즈, 속력, 방향)을 집어넣는다. 
     
    2. 낚시왕이 한 칸 열을 뒤로 이동하고 그래프를 돌면서 특정 열에 대한 생선을 잡는다.
     - 생선을 잡는 순간 break
    
    3. 특정 열에 대한 생선을 잡은 후에는 상어의 이동이 이루어진다.
     - 3-0) 상어의 위치를 저장할 비어있는 R*C 2차원 g 배열 생성 
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

input = sys.stdin.readline
R, C, M = map(int, input().split())

# 북 남 동 서
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

graph = [[list() for _ in range(C)] for _ in range(R)]

for _ in range(M):
    x, y, s, d, z = map(int, input().split())
    graph[x - 1][y - 1].append([z, s, d - 1])


def move_king():
    global king, weight

    king += 1

    for i in range(R):
        if graph[i][king]:
            weight += graph[i][king][0]
            break


def move_shark():
    g = [[list() for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j
                size, speed, d = graph[i][j][0]
                temp_speed = speed

                # 상어가 이동할 차례 ( 한 칸씩 이동 )
                while temp_speed > 0:
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 좌표에 벗어난다면 방향 이동
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        if d in [0, 2]:
                            d += 1
                        elif d in [1, 3]:
                            d -= 1
                        continue

                    # 좌표에 벗어나지 않다면 상어 이동
                    else:
                        x = nx
                        y = ny
                        temp_speed -= 1

                # 상어의 이동이 끝나면 최종좌표를 g 배열에 집어넣음
                g[x][y].append([size, speed, d])

    # 모든 상어의 이동이 끝나면 graph에 값 대입해주기
    for i in range(R):
        for j in range(C):
            graph[i][j] = g[i][j]

    # 한 좌표에 두 마리 상어가 있을 경우 가장 큰 상어만 남겨주기
    for i in range(R):
        for j in range(C):
            if len(graph[i][j]) >= 2:  # 상어가 2마리 이상이라면
                graph[i][j].sort(reverse=True)  # 첫 번째값(사이즈) 기준으로 역정렬

                while len(graph[i][j]) >= 2:
                    graph[i][j].pop()  # 사이즈가 가장 작은 것부터 빠져나감


king = -1
weight = 0
while True:
    move_king()
    move_shark()

    if king == C - 1:
        break

print(weight)
