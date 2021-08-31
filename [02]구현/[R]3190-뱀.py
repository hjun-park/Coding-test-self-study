import sys
from collections import deque

'''
    1) https://jjangsungwon.tistory.com/27
    2) https://esoongan.tistory.com/76
'''

# 방향을 전환하는 함수
# [동, 남, 서, 북 ]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# dy = [0, 1, 0, -1]
# dx = [-1, 0, 1, 0]


def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction


def start():
    direction = 0   # 초기 방향 설정
    time = 1    # 시간 설정
    x, y = 0, 0 # 초기 뱀 위치
    snake = deque([[x, y]])   # 뱀 좌표
    arr[x][y] = 2   # 초기 뱀 위치 설정

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 좌표 체크
        if 0 <= ny < N and 0 <= nx < N and arr[nx][ny] != 2:
            if arr[nx][ny] == 0:    # 사과가 없는 경우
                px, py = snake.popleft()    # 뱀 꼬리를 가져옴
                arr[px][py] = 0 # 꼬리 체거
                # 다음 칸을 뱀 이동 설정
                arr[nx][ny] = 2
                snake.append([nx, ny])
            if arr[nx][ny] == 1:    # 사과가 있는 경우
                snake.append([nx, ny])  # 뱀 좌표 추가
                arr[nx][ny] = 2 # 뱀 위치 추가 설정

            # 해당 시간이 되었다면
            if time in times.keys():
                direction = turn(direction, times[time])

            # 이동했더니 1초 지남
            time += 1

            # 실제 이동
            x, y = nx, ny

        # 좌표 범위를 벗어난 경우 시간만 초과
        else:
            print(time)
            break



if __name__ == '__main__':
    N = int(input())
    K = int(input())
    arr =[[0] * N for _ in range(N)]

    # 사과 좌표 입력
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a-1][b-1] = 1

    L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        times[int(X)] = C
    start()
