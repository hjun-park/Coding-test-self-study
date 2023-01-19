import sys
from collections import deque

input = sys.stdin.readline
# 좌 상 우 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N = int(input().rstrip())
board = [[0] * N for _ in range(N)]
board[0][0] = 1

# 사과
K = int(input().rstrip())
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

# 뱀 위치 추가
snake = deque()
snake.append((0, 0))

# 뱀 초 이동 경로 표시
L = int(input().rstrip())
# moves = defaultdict(int)
moves = deque()
for _ in range(L):
    X, C = input().split()
    moves.append((X, C))

time = 0
d = 2
while True:

    time += 1

    nx = snake[0][0] + dx[d]
    ny = snake[0][1] + dy[d]

    # 머리가 범위를 벗어 나면 break
    # TODO : 두 번째 실수 : range check
    if 0 > nx or N <= nx or 0 > ny or N <= ny:
        break

    # 이동 좌표 사과 있음
    if board[nx][ny] == 2:
        board[nx][ny] = 1
        snake.appendleft((nx, ny))

    # 이동 좌표 사과 없음
    elif board[nx][ny] == 0:
        board[nx][ny] = 1
        snake.appendleft((nx, ny))
        tail_x, tail_y = snake.pop()
        board[tail_x][tail_y] = 0

    # 이동 좌표 뱀 몸
    else:
        break

    # 시간 체크 후 이동
    # TODO : 처음 한 실수 : popleft 안 함
    if moves and time == int(moves[0][0]):
        _, dir = moves.popleft()
        if dir == 'D':
            d = (d + 1) % 4
        elif dir == 'L':
            d = (d - 1) % 4


print(time)