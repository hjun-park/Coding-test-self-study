import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

# 위 아래 왼쪽 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

'''
 - 번호 1 어른 상어는 가장 강해서 나머지 쫓기 가능
 - [맨 처음] 모든 상어가 자신 위치에 냄새를 뿌림
 - [1초 마다] 동시에 상하좌우로 인접 칸 이동 -> 자신의 냄새를 뿌림 (k라고 하자)
 - [1초 마다] 1초마다 k를 감소시키고 0이되면 냄새는 사라진다.
 - 모든 상어 이동 후 한 칸에 여러마리가 있다면 가장 작은 번호 제외한 모두 추방 
   (당연히 그 자리의 냄새도 새로 갱신)
 - 상어가 몇 마리 남아있는지 체크 ( 1마리라면 끝 )
 
 [이동방향 정하기]
 1. 냄새가 없는 칸 (여러칸 존재 시 특정한 우선순위에 따라 선택함)
  - 자신이 맨 처음에 보고 있는 방향을기준으로 우선순위 리스트를 참고한다
  - 우선순위 리스트를 돌면서 갈 수 있는 경우를 체크한다.
  - 4방향 다 없다면 (2번처럼 행동)
  - 있다면 그 방향으로 이동하고 보고 있는 방향 갱신
  
 2. 자신의 냄새가 있는 칸
'''

# M: 상어 / k: 상어 이동횟수
N, M, k = map(int, input().split())

# (상어 번호, 상어 방향)
graph = [[deque() for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] != 0:
            graph[i][j].append([line[j], 0])

# 초기 상어의 이동방향
temp = list(map(int, input().split()))

# 이동방향 집어넣어 줌
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            graph[i][j][0][1] = temp[(graph[i][j][0][0] - 1)]

# (상어 번호, 상어 냄새)
# spread = [[deque() for _ in range(N)] for _ in range(N)]
spread = [[[0, 0] for _ in range(N)] for _ in range(N)]

# 이동방향 결정 리스트
direction = [[] for _ in range(4) for _ in range(M)]

# 방향 추가
for shark in range(M):
    for d in range(4):
        direction[shark].append(list(map(int, input().split())))

# 1) 최초 상어가 있던 자리에 냄새를 뿌림
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            # spread[i][j].append([graph[i][j][0], k])
            spread[i][j][0] = graph[i][j][0]  # 냄새 주인
            spread[i][j][1] = k  # 냄새

for time in range(1000):
    # 2) 상어가 한 마리만 남았는지 체크, 1마리만 남았다면 time 출력
    cnt = 0
    for i in range(N):
        for j in range(N):
            # if graph[i][j]:
            cnt += len(graph[i][j])

    if cnt == 1:
        print(time)
        break

    copied_graph = deepcopy(graph)
    # 3) 상어 이동하기 (인접이동)(냄새체크)
    for x in range(N):
        for y in range(N):
            if graph[x][y]:
                # graph[i][j][0][1] : 자신의 방향
                # spread[i][j][0][1] : 상어의 냄새 시간초
                nx = x + dx[graph[x][y][0][1]]
                ny = y + dy[graph[x][y][0][1]]

                # 내 진행방향으로 이동 가능 시
                if 0 <= nx < N and 0 <= ny < N:
                    if spread[nx][ny][1] == 0:  # 냄새 없음 -> 이동
                        copied_graph[nx][ny].append(copied_graph[x][y].popleft())
                        break

                # 내 진행방향에 냄새가 있는 경우 이동방향을 새로 설정
                # direction[상어번호][상어이동방향]
                for d in direction[graph[x][y][0][0]][graph[x][y][0][1]]:
                    d -= 1  # 1 더해서 저장되어있기 때문에 1을 빼 주었음
                    # nx, ny 재설정
                    nx = x + dx[graph[x][y][0][1]]
                    ny = y + dy[graph[x][y][0][1]]

                    # 내 진행방향으로 이동 가능 시
                    if 0 <= nx < N and 0 <= ny < N:
                        if spread[nx][ny][1] == 0:  # 이동방향 변경, 냄새 없으면 이동
                            copied_graph[nx][ny].append(copied_graph[x][y].popleft())
                            break

                # 네 방향 확인 했음에도 불구하고 갈 곳이 없었다면 자신 냄새 쪽으로 이동
                for d in direction[graph[x][y][0][0]][graph[x][y][0][1]]:
                    d -= 1  # 1 더해서 저장되어있기 때문에 1을 빼 주었음
                    nx = x + dx[graph[x][y][0][1]]
                    ny = y + dy[graph[x][y][0][1]]

                    # 내 진행방향으로 이동 가능 시
                    if 0 <= nx < N and 0 <= ny < N:
                        if spread[nx][ny][0] == graph[x][y][0][0]:  # 자신 번호
                            copied_graph[nx][ny].append(copied_graph[x][y].popleft())
                            break

    # 4) 중첩한 상어 체크, 번호에 따른 쫓아내기

    # 5) spread를 한 번 돌며 냄새 감소 후 상어가 있는 자리에 냄새를 설치함

else:
    print(-1)
