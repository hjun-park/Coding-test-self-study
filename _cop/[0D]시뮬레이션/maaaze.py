import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

'''
    1. [판을 쌓는다] 순열을 사용하여 판을 쌓는다. (판을 쌓은 후 판 전체를 복사) 
    2. [판을 회전한다] 회전은 4번 가능, 재귀 사용하여 처음과 끝부분에 도달 가능해야만 다음 로직 가능  
        함수정의 : def logic(layer) (해당 계층에서 회전할 지 말지를 정하는 재귀식)
        base condition :  layer가 5일 때 검증하고 탈출구가 있으면 다음 수행 아니면 그냥 return
    3. [탈출구가 있는지 확인한다] bfs 순환
 
'''

# 시뮬레이션 브루트포스 BFS
# deque 사용
graph = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]

min_move = int(1e9)


# 하양 : o (1)
# 검은 : x (0)
# 탈출 불가능 -1

# 판 시계 반시계
def tilt():
    pass


# 판 회전 (브루트포스)
def rotate():
    pass

#  2. [판을 회전한다] 회전은 4번 가능, 재귀 사용하여 처음과 끝부분에 도달 가능해야만 다음 로직 가능
#         함수정의 : def logic(layer) (해당 계층에서 회전할 지 말지를 정하는 재귀식)
#         base condition :  layer가 5일 때 검증하고 탈출구가 있으면 다음 수행 아니면 그냥 return
def check_recursion(layer):
    pass

# 1. [판을 쌓는다] 순열을 사용하여 판을 쌓는다. (판을 쌓은 후 판 전체를 복사)
for p in permutations([x for x in range(5)]):
    for i in p:
        maze[i] = graph[i]

    check_recursion(0)


























