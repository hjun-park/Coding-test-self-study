import sys

# 시뮬레이션 문제는 종이에 그려보면서 푸는 것이 좋다.
# 뱀의 크기는 늘어나는게 아니고 좌표를 점령한다고 생각하면 된다.

n = int(input())  # 보드 크기 nxn
k = int(input())  # 사과의 개수 K
point = []

# 사과의 위치 입력받음
for i in range(k):
    a, b = map(int, input().split())
    print(a, b)
    point[a][b] = 1  # 사과는 1이라고 설정

# 뱀의 방향 회전 정보 입력
L = int(input())
# (X, C) : X초가 지난 뒤에 C는 L(왼쪽)인지 D(오른쪽)인지 방향 90도 회전
info = []  # 방향 회전 정보
for _ in range(L):
    x, c = map(int, input().split())
    info.append((int(x), c))

# 처음에는 동쪽을 보고 있으므로 [동, 남, 서, 북]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1  # 뱀의 머리 좌표
    point[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시 (사과는 1)
    direction = 0  # 처음에는 동쪽을 바라봄 [ 동1, 남2, 서3, 북4 ]
    time = 0  # 시작 후 지난 시간
    index = 0  # 다음에 회전 할 정보
    q = [(x, y)]  # 뱀이 차지 할 위치 정보 ( 좌표정보 ) - 꼬리가 앞쪽

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵의 범위 안이며, 뱀의 몸통이 없다면,
        if (1 <= nx <= n) and (1 <= ny <= n) and point[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if point[nx][ny] == 0:
                point[nx][ny] = 2
                q.append((nx, ny))  # 뱀 위치 좌표 추가
                px, py = q.pop(0)  #
                point[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 두기
            if point[nx][ny] == 1:
                point[nx][ny] = 2
                q.append((nx, ny))

        # 맵의 범위를 벗어나거나 뱀 스스로 부딪힌다면
        else:
            time += 1
            break

        x, y = nx, ny  # 다음 위치로 머리 이동
        time += 1

        if index < 1 and time == info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())
