import sys
from collections import deque

input = sys.stdin.readline

'''
    팁1 : 숫자의 자릿수가 다른 경우는 뒤에서부터 확인한다.
    
    배운점:
    0) 방향은 사전으로 정의한다.
        change_dir = {0: 1, 1: -1}
     
    1) 리스트를 rotate하고 싶을 때    
        q = deque()   
        q.append([1, 2, 3, 4])
        q[0].rotate(change_dir[d] * k)    # d의 방향대로 k만큼 rotate
    
    2) N까지의 숫자 중에서 x와 배수인 것을 확인하는 방법
        1. 0부터 N까지 순회하면서 x와 나누어 떨어지는지 확인한다.
            for i in range(1, N+1):
                if i % x == 0:
                print(f'x의 배수 {i}')
                
    3) 이차원 배열에서 0을 세는 방법
    N = 2
    graph = [[1, 0], [3, 4]]
    zero_cnt = sum([graph[i].count(0)] for i in range(N))
   
    4) q의 전체합을 구하는 방법
    q = ([1, 2, 3, 4])
    dividend = sum(sum(q, deque()))   
'''


def logic():
    # 1) 원판 회전
    for x, d, k in tilt:
        for i in range(N):  # 배수인 경우에만 원판 회전
            if (i + 1) % x == 0:
                q[i].rotate(change_dir[d] * k)

        temp = []
        # # 2, 3번 모두 양쪽방향 비교할 필요 없이 한 방향으로만 비교해도 된다.
        # 한 쪽만 비교해도 되는 이유는 ?????

        # 2) 다른 원판 인접한 숫자 체크 ( 인접한 노드는 temp 리스트만들어 좌표 담아주기 )
        for i in range(N - 1):  # n과 n+1 원판을 비교할 것이므로
            for j in range(M):
                # 해당 원판 값이 0이 아니면서 다음 인접한 원판 값과 동일한 경우 temp에 추가
                if q[i][j] and q[i + 1][j] == q[i][j]:
                    temp += ([i, j], [i + 1, j])

        # 3) 같은 원판 내에서 인접한 숫자 체크
        for i in range(N):
            for j in range(M):
                # 해당 원판 값이 0이 아니면서 바로 이전 원판값과 동일하면 temp에 추가
                if q[i][j] and q[i][j - 1] == q[i][j]:
                    temp += ([i, j - 1], [i, j])

        # 인접한 것들 중 동일한 숫자 모두 0 만들기
        for i, j in temp:
            q[i][j] = 0

        # 회전 후에 인접한 것이 없는 경우 ( temp가 비어 있다면 평균을 구해 값을 바꿔준다. )
        if not temp:
            zero_cnt = sum([q[i].count(0) for i in range(N)])
            divisor = N * M - zero_cnt
            dividend = sum(sum(q, deque()))

            # 나눌 것이 없다면 다음 회전으로 넘어감
            if not divisor:
                continue

            avg = dividend / divisor

            # 0이면 다음으로, 평균보다 작으면 1 더하고 크면 1 뺀다.
            for i in range(N):
                for j in range(M):
                    if not q[i][j]:
                        continue

                    if q[i][j] < avg:
                        q[i][j] += 1
                    elif q[i][j] > avg:
                        q[i][j] -= 1


# 방향의 경우 사전으로 정의해 놓는다.
change_dir = {0: 1, 1: -1}
N, M, T = map(int, input().split())  # 원판개수, 원판 최대 적힌 수, 회전 횟수
# i번째(원판번호) 줄에 적혀 있는 j번째 수

q = deque()
for _ in range(N):
    q.append(deque(map(int, input().split())))

tilt = [list(map(int, input().split())) for _ in range(T)]
logic()
print(sum(sum(q, deque())))
