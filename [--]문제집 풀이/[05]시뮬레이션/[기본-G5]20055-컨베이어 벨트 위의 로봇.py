import sys
from collections import deque

input = sys.stdin.readline

'''
    [참고] https://jainn.tistory.com/81
'''

# N: 칸 개수 / K: 내구도 0인 칸이 K개 이상이면 종료
N, K = map(int, input().split())

# 컨베이어 칸의 내구도
A = deque(map(int, input().split()))

# 로봇에 대한 정보 (위치)
robots = deque([False] * N)  # 맨 끝은 컨베이어가 내려가는 부분의 시작점
robots[-1] = False  # 컨베이어의 끝은 항상 -1로 설정

step = 0
while True:

    # 1) 한 칸 회전
    robots.rotate(1)
    A.rotate(1)
    robots[-1] = False  # 로봇 이동 후 내려가는 부분 내려주기

    # 2) 벨트의 맨 뒤부터 확인하면 먼저 벨트에 올라간 로봇을 확인할 수 있음
    if sum(robots):  # 로봇이 존재한다면 이동 시작
        for i in range(N - 2, -1, -1):
            # 한 칸 이동할 수 있는지 체크 후 이동 (현재 로봇 있고 다음엔 없으며 내구도 존재)
            if robots[i] and not robots[i + 1] and A[i + 1] > 0:
                robots[i + 1] = True
                robots[i] = False
                A[i + 1] -= 1
        # 모든 로봇 이동 후 맨 끝 로봇은 컨베이어에서 내리므로 False 처리
        robots[-1] = False  # 로봇을 내림

    # 3) 올리는 위치 칸 내구도가 0이 아니라면 그 위치에 로봇을 올림
    if A[0] > 0 and not robots[0]:
        robots[0] = True
        A[0] -= 1

    # 4) 0의 개수를 세기
    step += 1
    if A.count(0) >= K:
        print(step)
        break

