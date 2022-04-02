# import heapq
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 양분의 정보를 담고 있는 리스트
graph = [[5] * N for _ in range(N)]

# 양분 추가 시 참고하는 리스트
A = [list(map(int, input().split())) for _ in range(N)]

# 나무의 정보를 담고 있는 리스트
trees = [[deque() for _ in range(N)] for _ in range(N)]
dead_trees = [[list() for _ in range(N)] for _ in range(N)]

# x, y, 나이
# 2) 나무 정보 입력
for i in range(M):
    x, y, a = map(int, input().split())
    trees[x - 1][y - 1].append(a)
    # heapq.heappush(trees[x - 1][y - 1], a)

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

'''
    [요약]
    1. 모든 칸에 5만큼 양분 포함 ( N x N )
    2. M개의 나무를 구입하여 나무 재테크 시작 ( 한 공간에 여러 개 나무 존재 가능 )
    3. 4계절을 거치며 아래 과정 반복(K만큼 반복)
    4. 봄 (흡수)
     4-1. 나무 자신 나이만큼 양분 먹고 나이 1 증가
          한 칸에 여러 개 나무가 있다면 가장 나이가 어린 나무부터 양분을 먹음
     4-2. 여러 개 있어도 쭉 먹다가 양분이 부족한 칸의 나무는 즉시 죽는다.
    5. 여름 (처리)
     5-1. 죽은 나무를 양분 처리 ( 죽은 나무 나이 // 2 = 양분 )
    6. 가을 (번식)
     6-1. 나무의 나이가 5의 배수라면 8개 칸에 나이 1인 나무 생성
    7. 겨울 (보충)
     7-1. A[r][c] 만큼 양분추가
    
    [풀이] - heapq로 풀면 안 된다.
    1) 입력 및 N 리스트 생성
    2) 나무 정보 입력
    3) K만큼 반복 하면서 루프 실행
    3-1) 루프 순회 -> 나무 있다면 빼냄 
      -> graph와 비교해서 양분 충분하면 graph에서 양분 차감
      -> 양분을 먹은 나무는 따로 temp 리스트에 저장
      -> 양분이 부족한 나무는 전체나이를 구하고 // 2 해서 양분 구하기  (nut) 
      -> temp 리스트로 heapq를 대체 (자란 나무들 대체)
      -> graph 해당 칸에는 nut을 더해주기 (죽은 나무 양분작업) 
    3-2) 다시 루프 순회하면서 5의 배수가 있는 나무가 있으면 8개 칸에 나이 1 나무 생성
    3-3) graph에 A[r][c]만큼 양분 추가
    
    
    [주의점]
    1. heapq로 하면 시간초과, deque()
'''

# 3) K만큼 반복 하면서 루프 실행
for _ in range(K):

    # ============================================
    # (1) deque()로 푼 봄-여름 부분
    # ============================================
    # [봄 작업]
    # 3-1) 루프 순회
    for i in range(N):
        for j in range(N):
            N = len(trees[i][j])
            for k in range(N):
                # 양분보다 나무의 나이가 더 큰 경우는 나무가 죽음
                if graph[i][j] < trees[i][j][k]:
                    for _ in range(k, N):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break

                # 양분 수용 가능한 경우
                else:
                    graph[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    # [여름 작업]
    for i in range(N):
        for j in range(N):
            while dead_trees[i][j]:
                graph[i][j] += dead_trees[i][j].pop() // 2

    # [가을] 다시 루프 순회 하면서 5의 배수가 있는 나무가 있으면 8개 칸에 나이 1 나무 생성
    for i in range(N):
        for j in range(N):
            cnt = 0
            for age in trees[i][j]:
                if age % 5 == 0:
                    cnt += 1

            for m in moves:
                nx = i + m[0]
                ny = j + m[1]

                if 0 <= nx < N and 0 <= ny < N:
                    for _ in range(cnt):
                        trees[nx][ny].appendleft(1)

    # print('>>> 가을작업')
    # for row in trees:
    #     print(*row)

    # [겨울] graph에 A[r][c]만큼 양분 추가
    for i in range(N):
        for j in range(N):
            graph[i][j] += A[i][j]

    # print('>>> 겨울작업')
    # for row in graph:
    #     print(*row)

# 나무 개수 카운트
cnt = 0
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            cnt += len(trees[i][j])

print(cnt)

# ============================================
# (1) Heapq로 풀어서 시간초과가 나왔던 봄-여름 부분
# ============================================
# ate_trees = []
# total_age, nut = 0, 0
#
# while trees[i][j]:
#     # print(f'있는 나무 찾음{i}, {j}')
#     # -> 나무 있다면 빼냄
#     # age = heapq.heappop(trees[i][j])
#     age = trees[i][j].pop()
#
#     # -> graph와 비교해서 양분 충분하면 graph에서 양분 차감
#     if graph[i][j] >= age:
#         graph[i][j] -= age
#         # -> 양분을 먹은 나무는 따로 나이 1 더해서 ate_trees 리스트에 저장
#         ate_trees.append(age + 1)
#
#     # -> 양분이 부족하면 그 이후도 부족하기 때문에
#     # -> 리스트에 남아있는 요소들을 모두 더하고 // 2 해서 양분 구하기 (nut)
#     # [https://www.acmicpc.net/board/view/76792]
#     # -> sum(trees[i][j])로 했는데 값이 무한히 커지는 경우 오차가 발생할 수 있음
#     # -> 따라서 for문으로 각각 더함
#     else:
#         total_age += age // 2
#         # total_age += sum(trees[i][j])
#
#         while trees[i][j]:
#             total_age += trees[i][j].pop() // 2
#
#         # for tree in trees[i][j]:
#         #     total_age += tree // 2
#
#         # nut = total_age // 2
#         # trees[i][j] = []
# else:  # 루프를 다 돌고나서
#     # print(f' ################### 완료')
#     # print(f' ################### 완료')
#     # ate_trees 리스트로 heapq를 대체 (자란 나무들 대체)
#     trees[i][j] = deque(deepcopy(ate_trees))
#
#     # -> [여름] graph 해당 칸에는 nut을 더해주기 (죽은 나무 양분작업)
#     # graph[i][j] += nut
#     graph[i][j] += total_age

# print('>>> 여름작업')
# for row in trees:
#     print(*row)
