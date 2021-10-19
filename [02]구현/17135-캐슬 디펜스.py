import sys
from copy import deepcopy
from heapq import heappush, heappop
from itertools import combinations

input = sys.stdin.readline

# 행, 열, 궁수공격거리제한
N, M, D = map(int, input().split())

# 적이 위치한 그래프
graph = [list(map(int, input().split())) for _ in range(N)]
arr = []

castle = [i for i in range(M)]  # 궁수를 놓을 리스트
archer_cb = tuple(combinations(castle, 3))  # 궁수위치(y좌표만) 뽑아놓은 tuple
answer = 0

'''
  핵심
    1. 가장 왼쪽에 있는 적이란 의미는 우선순위 큐를 이용하면 된다.
'''

'''
  요약
    1. 궁수 3명 배치 조합 생성
    2. 적의 개수를 세고 0이 아니라면 적을 공격하는 단계로 이동
      - 0일 경우 적의 개수를 반환
    3. [적 공격단계] comb 리스트에서 궁수 3명을 각각 꺼낸다. 
       그리고 pq 리스트 생성한다.attacked_list, remove_list도 생성, 제거한 적 cnt 생성
     - for i in range(n-1, -1, -1) for j in range(M) 이런순으로 도는데 그 이유는
        거리가 가까운 곳부터 공격을 하기 위함
     - 이후 거리계산을 하고, 거리가 D보다 가까우면 pq라는 데에 heap을 이용하여  거리, x, y 좌표를 집어넣는다.
     - 한 궁수의 공격이 끝나고 hq가 있다면 그 내용을 꺼내서 remove_list에 x, y좌표 등록
     - 모든 궁수의 공격과 적 제거 등록이 끝나고 remove_list를 통해서 attacked리스트를 True변경, cnt++
       당연히 복사된 arr도 0으로 표기함으로써 적 제거 완료     
    4. 적 이동
      - 복사된 배열의 맨 끝부분을 0으로 초기화 ( 굳이 해야할까 ? )
      - for i in range(-1, -n, -1): 가장 끝부터 처음순으로 돌면서 
         arr[i] = arr[i-1] 
      - 복사된 배열의 맨 첫부분을 0으로 초기화
'''


def move_enemy():
    global arr
    arr[-1] = [0 for _ in range(M)]

    for i in range(-1, -N, -1):
        arr[i] = arr[i - 1]

    arr[0] = [0 for _ in range(M)]


def attack_enemy(idx):
    global arr
    # attacked = [[False] * M for _ in range(N)]  # 궁수가 공격한 적 위치
    attacked = [[False for _ in range(M)] for _ in range(N)]
    remove_list = []
    cnt = 0  # 공격한 적의 수

    for archer_pos in archer_cb[idx]:
        hq = []

        for i in range(N - 1, -1, -1):
            for j in range(M):
                if arr[i][j] == 1:  # 거리에 적이 있다면 그 적과의 거리 계산
                    distance = abs(N - i) + abs(archer_pos - j)

                    # heap에 저장할 때 거리,그 다음으로 y좌표값을 집어넣음
                    # 그 이유는 거리가 가까워야 공격하고 왼쪽을 먼저 공격하기 때문이다.
                    if distance <= D:
                        heappush(hq, [distance, j, i])

        # 한 궁수의 공격이 끝나면 remove_list에 적 위치 추가
        if hq:
            _, y, x = heappop(hq)
            remove_list.append((x, y))

    # 모든 궁수의 공격이 끝나면 remove 리스트를 참고해서 공격당한 적을 셈 (remove_list는 중복으로 공격당한 적이 있음 )
    for x, y in remove_list:
        if not attacked[x][y]:
            cnt += 1
            attacked[x][y] = True
            arr[x][y] = 0

    return cnt


def get_enemy_count():
    global arr
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1

    return cnt


def simulation(archer_case_index):
    cnt = 0

    while get_enemy_count() != 0:
        cnt += attack_enemy(archer_case_index)
        move_enemy()

    return cnt


for idx in range(len(archer_cb)):
    arr = [[graph[i][j] for j in range(M)] for i in range(N)]
    # arr = deepcopy(graph)
    cnt = simulation(idx)
    answer = max(answer, cnt)

print(answer)
