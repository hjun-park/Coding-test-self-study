import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M, G, R = map(int, input().split())

# 0: 호수 / 1: 배양액 못 뿌리는 땅 / 2: 배양액 뿌리는 땅
graph = [list(map(int, input().split())) for _ in range(N)]
# 0: 없음 / 1: Green / 2: Red / 3: 꽃
field = [[0] * M for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
 # 1
'''
    [요약]
    1. 배양액은 황토색 칸에만 뿌릴 수 있음 / 하얀색은 뿌릴 수 없음 / 호수는 배양액이 못 감
    2. 배양액은 상하좌우로 퍼져나감
    3. 배양액이 동시에 만난 경우에만 꽃이 피게 된다.
    4. 꽃 부분은 배양액이 더이상 퍼져나가지 않음
    - 최대 꽃의 개수를 구함
    
    [풀이] - 백트래킹
    1. 녹색 배양액을 먼저 셋팅하고, 빨간색 배양액을 다음으로 셋팅
    2. cnt == R + G 라면,  DFS 로직을 시작한다.
    3. cnt != R + G 라면, 계속해서 배양액을 뿌린다.
     - 녹색 배양액을 다 설치했는지 확인, 녹색 배양액을 먼저 설치하고 빨간 배양액 설치
     
    [함수 정의]
    
    [base condition]
    if cnt == R + G: 
        start_bfs()
        
    
    [recursion]
'''
is_spread = False

result = -1
g_cnt = 0
r_cnt = 0


def bfs(start_x, start_y, color, color_field):
    global is_spread

    q = deque()
    q.append((start_x, start_y))

    visited = [[False] * M for _ in range(N)]
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                # 방문한 적이 없으면서,
                if not visited[nx][ny]:
                    # 호수가 아니며, 배양액이 없는 경우
                    if graph[nx][ny] != 0 and color_field[nx][ny] == 0:
                        color_field[nx][ny] = color  # 배양액을 퍼트림
                        # q.append((nx, ny))
                        visited[nx][ny] = True


def spread():
    global field, is_spread, cnt, result
    idx = 0

    temp = deepcopy(field)

    while True:
        copied_field = deepcopy(temp)
        cnt = 0
        is_spread = False
        # 1) field로부터 green_field, red_field 복사
        green_field = deepcopy(copied_field)
        red_field = deepcopy(copied_field)

        # 1-1) green, red의 좌표를 구함
        green, red = [], []

        for i in range(N):
            for j in range(M):
                if copied_field[i][j] == 1:  # green
                    green.append((i, j))
                elif copied_field[i][j] == 2:  # red
                    red.append((i, j))

        # 2) green, red를 순회하면서 배양액을 퍼뜨림
        for x, y in green:
            bfs(x, y, 1, green_field)

        for x, y in red:
            bfs(x, y, 2, red_field)

        idx += 1
        # print(f'========= {idx}번 째 =========')
        # print('배양액 퍼트린 결과 - Green')
        # for row in green_field:
        #     print(*row)
        # print('배양액 퍼트린 결과 - Red')
        # for row in red_field:
        #     print(*row)

        # copied_field = deepcopy(field)
        # 3) 인덱스 돌면서 겹치는 부분은 꽃으로 만들고 나머지는 그대로 field에 반영
        for i in range(N):
            for j in range(M):
                # 겹치는 부분 -> 꽃
                if green_field[i][j] == 1 and red_field[i][j] == 2:
                    copied_field[i][j] = 3

                elif green_field[i][j] == 1:
                    copied_field[i][j] = 1

                elif green_field[i][j] == 2:
                    copied_field[i][j] = 2

                else:
                    continue

        for i in range(N):
            for j in range(M):
                if temp[i][j] != copied_field[i][j]:
                    is_spread = True
                    break
            if is_spread:
                break

        # print('복사필드')
        # print(copied_field)
        # print('일반필드')
        # print(field)
        # print(is_spread)
        #
        # idx += 1
        #
        # print(f'idx = {idx}')
        # if idx >= 2:
        #     break

        if not is_spread:
            # print(f'>>>> 배양액이 더 이상 퍼질 수 없어 종료')
            for i in range(N):
                for j in range(M):
                    if copied_field[i][j] == 3:
                        cnt += 1
            # print(f'>>>> 꽃의 개수 = {cnt}')
            # print()
            result = max(result, cnt)
            break

        temp = deepcopy(copied_field)



def dfs():
    global g_cnt, r_cnt, field
    if R + G == g_cnt + r_cnt:
        # print('***** 필드 상태 *****')
        # for row in field:
            # print(*row)
        spread()
        return

    else:
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 2 and field[i][j] == 0:
                    if g_cnt < G:  # 그린 설치 가능
                        field[i][j] = 1
                        g_cnt += 1
                    else:  # 레드 설치 가능
                        field[i][j] = 2
                        r_cnt += 1

                    dfs()
                    # 필드 복구
                    if r_cnt > 0:
                        r_cnt -= 1
                        field[i][j] = 0
                    else:
                        g_cnt -= 1
                        field[i][j] = 0


dfs()
print(result)
