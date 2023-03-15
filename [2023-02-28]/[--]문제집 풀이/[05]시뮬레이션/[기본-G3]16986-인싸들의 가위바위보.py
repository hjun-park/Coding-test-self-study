import sys
from itertools import permutations

input = sys.stdin.readline

'''
    1 3명이서의 인싸 가위바위보
    2 1:1로 토너먼트 진행
    3 무승부 발생 시 : 뒤에 있는 사람이 이김
    4 이전 경기의 승자와 경기 진행 X 사람의 재진행 
    5 특정 사람이 합의된 승수를 달성할 때까지 3을 반복 -> 우승자
    
    지우가 모든 손동작을 다르게 내어 우승할 수 있는지 판단하는 프로그램 제작
    경기 진행 순서 [지우 / 경희 / 민호]
'''

# 손동작 수, 필요 승수
N, K = map(int, input().split())

# 가위바위보 손동작 수에 대한 상성표 ( Aij가 2: i가 j를 이김 / 1: 비김 / 0: 진다)
graph = [list(map(int, input().split())) for _ in range(N)]

# 경희, 민호
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

# 손 동작 액션 수
actions = [x + 1 for x in range(N)]


# 가위바위보 플레이어 2명 / 손동작 인덱스 / 승점 / 손동작 리스트
def dfs(pl1_num, pl2_num, rnd, scores, hand_list):
    global result
    # print(scores)
    if scores[0] == K:  # 지우 승
        # result = 1
        return 1
    if scores[1] == K or scores[2] == K:  # 경희, 민호 승
        return 0
    if rnd[0] == N:  # 다음 번에 낼 손동작 인덱스가 N이라면 지우는 더 낼 것이 없으므로 return
        return 0

    # 가위바위보를 하지 않는 pl3의 번호 지정
    pl3_num = 3 - (pl1_num + pl2_num)

    # player 1, 2의 손동작 리스트에서 해당 라운드에 속하는 손동작을 꺼냄 (+1 증가해 있으니 1을 감소)
    p1_hand = hand_list[pl1_num][rnd[pl1_num]] - 1
    p2_hand = hand_list[pl2_num][rnd[pl2_num]] - 1

    # 경기한 친구들만 라운드 증가
    rnd[pl1_num] += 1
    rnd[pl2_num] += 1

    # pl1이 이겼을 경우 (비길 경우 뒤에 있는 사람이 승)
    if graph[p1_hand][p2_hand] == 2 or (graph[p1_hand][p2_hand] == 1 and pl1_num > pl2_num):
        # print('p1 승')
        scores[pl1_num] += 1
        dfs(pl1_num, pl3_num, rnd, scores, hand_list)

    # pl2가 이겼을 경우
    elif (graph[p1_hand][p2_hand] == 1 and pl1_num < pl2_num) or graph[p1_hand][p2_hand] == 0:
        # print('p2 승')
        scores[pl2_num] += 1
        dfs(pl2_num, pl3_num, rnd, scores, hand_list)


for p1 in permutations(actions, N):  # 지우가 게임에서 선택하는 손 동작 수
    player = [p1, p2, p3]  # 20게임에서 플레이어가 선택하는 손동작
    action_index = [0, 0, 0]  # 지우, 경희, 민호가 다음 번에 낼 손동작 index
    win = [0, 0, 0]  # 지우, 경희, 민호 이긴 횟수

    # 처음 가위바위보는 0과 1이 출발
    result = 0
    print(dfs(0, 1, action_index, win, player))
    # 주석된 라인을 사용할 경우 return 값이 None임 (함수 끝까지 실행 됨으로)
    # if dfs(0, 1, action_index, win, player) == 1:
    if result == 1:
        print(1)
        break
else:
    print(0)
