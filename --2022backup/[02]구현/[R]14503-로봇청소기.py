import sys

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []

# 0) 좌표 설정 - 문제에서 요구하는대로 ( 북, 동, 남, 서 )
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1) 그래프 입력 받기
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 2) 방향을 좌측으로 돌리는 함수
def turn_left():
    global d
    d = (d-1) % 4  # 1을 빼면 왼쪽으로, 더하면 오른쪽으로 돈다.

# 3) count 1로 초기화(시작지 청소하고 시작하므로) 및 시작지 x, y로 초기화
count = 1
x, y = r, c

# 0: 미청소, 1: 벽, 2: 청소처리(방문처리)
# 4) 해당 시작 좌표 값은 2로 초기화 ( 청소 처리 )
graph[x][y] = 2


while True:
    check = False # 방문한 칸이 있는지 없는지 유무 파악 변수
    # 5) 4방향을 돌면서 nx, ny를 지정하여 그래프를 벗어나는지 확인
    # 5-1) 벗어나지 않는다면, count += 1, 그리고 방문처리(2)를 해 줌
    for i in range(4):
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                count += 1
                # 실제 이동
                x, y = nx, ny
                check = True   # 칸이 있다는 의미 처리
                break

    # 6) check값 확인, False라면 4방향 모두 이동을 못하는 경우이므로 nx, ny로 후진좌표 계산
    if not check:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 2:  # 청소한 자리인 경우 이동
                x, y = nx, ny
            elif graph[nx][ny] == 1:    # 벽인 경우 출력, 종료
                print(count)
                break




