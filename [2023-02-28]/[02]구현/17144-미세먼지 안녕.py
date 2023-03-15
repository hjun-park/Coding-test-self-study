import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
air_purifier = []  # ??

A = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기는 1열에 존재하므로 여러 행을 찾아보면 된다.
up = -1
down = -1
for i in range(R):
    if A[i][0] == -1:
        up = i  # 공기 청정기 윗부분
        down = i + 1  # 공기 청정기 아랫부분
        break


# 구현요소
'''
참고 : https://kyun2da.github.io/2021/04/20/brownsmog/    // 공기청정기
       https://yuuj.tistory.com/96  // 미세먼지 계산
1) 미세먼지 확산
2) 공기청정기 바람의 이동

핵심:
    공기청정기 윗바람, 아랫바람의 이동방식
    -> 윗바람 : 우, 상, 좌, 하
    -> 아랫바람 : 우, 하, 좌, 상
    
    공기청정기 바람 이동은 이동방향대로 한 칸씩 가면서 이전과 바꾸어 주는 방식
'''


# 미세먼지 확산
def spread_fine_dust():
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    # 계산값 영향 안 받게 새로운 배열 생성
    # 확산 배열
    new = [[0] * C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if A[x][y] >= 5:  # 5로 나누니까 5 이상 수에만 연산이 의미 있음
                count = 0

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < R and 0 <= ny < C:
                        if A[nx][ny] != -1:
                            new[nx][ny] += A[x][y] // 5
                            count += 1

                A[x][y] = A[x][y] - (A[x][y] // 5 * count)

    # 두 배열 합침
    for i in range(R):
        for j in range(C):
            A[i][j] += new[i][j]


#  -> 윗바람 : 우, 상, 좌, 하
def move_air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    before = 0
    d = 0
    x, y = up, 1  # 공기청정기 처음 바람의 위치

    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if x == up and y == 0:  # 공기청정기 위치로 다시 온 경우 종료
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d += 1  # 방향 전환
            continue

        A[x][y], before = before, A[x][y]

        x = nx
        y = ny


# -> 아랫바람 : 우, 하, 좌, 상
def move_air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    before = 0
    d = 0
    x, y = down, 1  # 공기청정기 처음 바람의 위치

    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if x == down and y == 0:  # 공기청정기 위치로 다시 온 경우 종료
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d += 1  # 방향 전환
            continue

        A[x][y], before = before, A[x][y]

        x = nx
        y = ny


# 미세먼지 파악
for _ in range(T):
    # 미세먼지 이동
    spread_fine_dust()

    # 공기청정기 작동
    move_air_up()
    move_air_down()

answer = 0
for i in range(R):
    for j in range(C):
        if A[i][j] > 0:
            answer += A[i][j]

print(answer)
