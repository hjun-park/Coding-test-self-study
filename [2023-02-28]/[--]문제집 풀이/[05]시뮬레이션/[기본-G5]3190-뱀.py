import sys
from collections import deque

input = sys.stdin.readline

'''
  1) 뱀의 길이 1, 처음 오른쪽 ( 뱀 위치 0, 0 //  )
  2) 매 초마다 이동 룰
   2-1) (현재 머리 몸통으로 교체 후 머리를 다음칸 위치) - 다음 칸을 추가만 하면 됨.
   2-2) (이동한 칸 if 사과 then 사과만 X)
   2-3) (이동한 칸 if not 사과 then 맨 끝 꼬리 X ) 
  3) 벽 or 자기자신 부딪히면 끝

  사과 = 1
  뱀 = 2
  빈 칸 = 0
'''

N = int(input().rstrip())
K = int(input().rstrip())  # 사과
graph = [[0] * N for _ in range(N)]

# 사과 마킹
# apples = [list(map(int, input().split())) for _ in range(K)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

L = int(input().rstrip())  # 뱀
graph[0][0] = 2
snake = deque()
snake.append((0, 0))
dirs = deque((input().split()) for _ in range(L))

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0  # 현재 뱀의 머리 방향 위치


def move():
    # 뱀의 머리
    x, y = snake[0][0], snake[0][1]
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 2:  # 범위 내 + 자기 몸 안 부딪힘

        # if not graph[nx][ny] != 2:  # 자기 몸에 안 부딪힘
        # 사과가 있는 경우
        # print(f'기존 뱀: {snake}')
        if graph[nx][ny] == 1:
            # print(f'{(nx, ny)} 사과 존재, 사과를 먹음')
            graph[nx][ny] = 2  # 뱀이 먹음

        # 사과가 없는 경우 (꼬리 제거)
        elif graph[nx][ny] == 0:
            # 꼬리 제거
            # print(f'사과가 없음')
            sx, sy = snake.pop()
            graph[sx][sy] = 0

        # 공통파트: 머리를 추가
        snake.appendleft((nx, ny))
        graph[nx][ny] = 2

        # print(f'뱀은 {(x, y)} -> {(nx, ny)} 이동, 길이 : {len(snake)}')
        # print(f'이후 뱀: {snake}')
        return 0

    else:
        return -1


cnt = 0
while True:

    cnt += 1
    # print()
    # print(f'>>> 현재시간: {cnt}')
    # 뱀 이동
    if move() == -1:  # 게임 끝
        print(cnt)
        break

    # 만약 해당 초 경과 시 방향 전환
    if dirs and cnt == int(dirs[0][0]):
        _, new_dir = dirs.popleft()

        if new_dir == 'L':
            d = (d - 1) % 4

        elif new_dir == 'D':
            d = (d + 1) % 4

        # print(f'{cnt} 방향회전 : {d}')
