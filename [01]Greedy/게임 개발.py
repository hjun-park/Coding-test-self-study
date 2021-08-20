import sys

# =================================================
# 1. 기본 정보 입력 및 입력값 초기화
# =================================================
n, m = map(int, sys.stdin.readline().split())

# 방문한 위치를 저장하기 위한 배열 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 좌표를 입력받음
x, y, direction = map(int, sys.stdin.readline().split())

# 현재 서 있는 곳은 방문처리
d[x][y] = 1

# 전체 맵 정보를 입력받음
map_info = []
for i in range(n):
    map_info.append(list(map(int, sys.stdin.readline().split())))

# =================================================
# 2. 방향 초기화
# =================================================
# [북, 동, 남, 서]
dx = [-1, 0, 1, 0]  # 북, 남방향 이동은 x축 좌표가 변함 (x, y)
dy = [0, -1, 0, 1]  # 동, 서방향 이동은 y축 좌표가 변함 (x, y)


# 왼쪽으로 회전 시 방향 지정
def turn_left():
    global direction

    direction -= 1
    if direction == -1:  # 모든 방향을 순회했을 때
        direction = 3


# =================================================
# 3. 시뮬레이션
# =================================================
count = 1  # 캐릭터가 방문한 칸의 수
turn_time = 0

while True:
    turn_left()
    # 해당 방향으로 이동 시 예상 방향, 거리 측정
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 방문하지도 않았으며 (d), 해당 위치는 바다가 아님 (map_info)
    if d[nx][ny] == 0 and map_info[nx][ny] == 0:
        d[nx][ny] = 1   # 방문처리
        x = nx
        y = ny  # 이동처리
        count += 1  # 방문칸 수 증가
        turn_time = 0   # 방향 초기화
    else:
        turn_time += 1  # 방향증가

    if turn_time == 4:  # 네 방향 모두 갈 수 없는 경우
        # 뒤로 가기 위해 좌표 지정
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동
        if map_info[nx][ny] == 0:
            x = nx
            y = ny

        # 뒤에도 바다라면
        else:
            break
        turn_time = 0

# 정답 출력
print(count)



