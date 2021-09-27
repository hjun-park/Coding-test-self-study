import sys
from collections import deque

'''
    https://soohee410.github.io/coding12
    1) 각 칸에 도달하기 위한 최소 주사위 횟수를 설정함
    # v번째 칸에 도달하기 위한 최소 주사위 횟수는 result
    saved_min_dice[v] = result
    
    2) 해당 칸에 도달하면 어디로 이동하는 지에 대한 경로를 설정
    # x 위치에 도달했다면 y로 이동
    stairs_and_snakes[x] = y
'''

input = sys.stdin.readline

N, M = map(int, input().split())

min_value = 1e9

# x에 도착하면 y로 이동한다.
stairs_and_snakes = list(range(101))
saved_min_dice = [101] * 101
for _ in range(N+M):
    x, y = map(int, input().split())
    stairs_and_snakes[x] = y


def bfs():
    q = deque()
    q.append(1)

    # 시작지
    saved_min_dice[1] = 0

    while q:
        v = q.popleft()

        if saved_min_dice[v] >= saved_min_dice[100]:
            continue

        for i in range(1, 7):
            if v + i > 100:  # 100칸 을 넘어가면 생략
                continue

            # 100을 안 넘는 경우
            num = stairs_and_snakes[v + i]

            # 방문하지 않은 경우
            if saved_min_dice[num] == 101:
                q.append(num)
                # 방문 예정지의 주사위 최소 주사위 횟수 = 이전 + 1
                saved_min_dice[num] = saved_min_dice[v] + 1

    return saved_min_dice[100]


print(bfs())
