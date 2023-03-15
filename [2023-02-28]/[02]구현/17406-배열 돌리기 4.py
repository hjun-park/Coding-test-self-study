import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
r_info = []
for _ in range(K):
    r, c, s = map(int, input().split())
    r_info.append([r - 1, c - 1, s])

k_count = [False] * K
'''
    구현 1: 회전연산
    구현 2: 최솟값 연산
    
    1) 입력값 저장
    2) dfs 를 통해 회전순서를 찾습니다. ( 백트래킹 )
      -> 회전 순서에 따라서 회전 결과가 달라지기 때문
      -> 회전 순서는 deque로 관리합니다.
    3) rotate에서 회전을 구현합니다, lx, ly, rx, ry 좌표를 저장하고 A를 A2로 복사합니다.
    4) 한 칸 한 칸 돌면서 before 값을 갱신시킵니다. 
    5) 한 바퀴 다 돌게되면 lx, ly는 +1, rx,ry는 -1 하여 회전 범위를 좁혀줍니다.
    6) 이를 반복하면서 lx >= rx, ly >= ry 되기까지 반복합니다.
    7) row 합을 구합니다. 그 중 최소는 따로 저장합니다.
    8) 순열의 모든 경우를 확인 후에 결과 중에서도 가장 최소를 출력합니다.

'''

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 회전하며 최솟값을 건짐
def rotate(q2):
    A2 = deepcopy(A)
    while q2:  # 회전횟수만큼 회전
        x, y, z = q2.popleft()
        lx, ly, rx, ry = x - z, y - z, x + z, y + z

        while True:  # lx >= rx, ly >= ry가 될 때까지 반복
            if lx >= rx or ly >= ry:
                break

            # 회전할 시작값 지정
            start_x, start_y, before = rx, ry, A2[rx][ry]
            d = 0  # >> TPS: 한 방향으로 쭉 나가기 위해서는 for문 대신 while문에다가 d변수 선언
            while True:  # 한바퀴 다 돌고 범위가 좁혀지면 좁혀진 값이 유효한지 확인
                nx = start_x + dx[d]
                ny = start_y + dy[d]

                # 이동할 범위가 범위 내라면 값 스왑, 이동
                if lx <= nx <= rx and ly <= ny <= ry:
                    before, A2[nx][ny] = A2[nx][ny], before
                    start_x, start_y = nx, ny

                    if (start_x, start_y) == (rx, ry):  # 이동한 방향이 시작지라면
                        # 회전하는 범위를 좁혀줌
                        lx += 1
                        ly += 1
                        rx -= 1
                        ry -= 1
                        break

                else:  # 범위를 벗어난다면
                    d += 1  # 방향 이동
                    continue

    # 회전이 다 끝나면 최솟값을 구함
    temp = int(1e9)
    for row in A2:
        temp = min(temp, sum(row))

    return temp


q = deque()
min_value = int(1e9)


# 회전하는 모든 경우의 수를 찾음 (백트래킹)
def dfs(cnt):
    global min_value

    # rotate 대상 개수를 만족한다면 rotate 시행
    if cnt == K:
        q2 = deepcopy(q)
        min_value = min(min_value, rotate(q2))
        return
    else:
        for i in range(K):
            if k_count[i]:  # 큐에 값이 있는 경우
                continue

            k_count[i] = True
            q.append(r_info[i])
            dfs(cnt + 1)
            k_count[i] = False
            q.pop()  # 빠져나오면 다시 복구


dfs(0)
print(min_value)
