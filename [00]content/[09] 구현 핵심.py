import sys
from collections import deque

input = sys.stdin.readline


# =============================================================== #

# [G3]17822-원판돌리기 ( https://www.acmicpc.net/problem/17822 )
    # 팁1 : 숫자의 자릿수가 다른 경우는 뒤에서부터 확인한다.

N = 2
d = 1
k = 1
x = 3
# 배운점:
# 0) 방향은 사전으로 정의한다.
change_dir = {0: 1, 1: -1}

# 1) 리스트를 rotate하고 싶을 때
q = deque()
q.append([1, 2, 3, 4])
q[0].rotate(change_dir[d] * k)    # d의 방향대로 k만큼 rotate

# 2) N까지의 숫자 중에서 x와 배수인 것을 확인하는 방법
    # 1. 0부터 N까지 순회하면서 x와 나누어 떨어지는지 확인한다.
    for i in range(1, N+1):
        if i % x == 0:
            print(f'x의 배수 {i}')

# 3) 이차원 배열에서 0을 세는 방법
graph = [[1, 0], [3, 4]]
zero_cnt = sum([graph[i].count(0)] for i in range(N))

# 4) q의 전체합을 구하는 방법
q = ([1, 2, 3, 4])
dividend = sum(sum(q, deque()))

# =============================================================== #

# [S3]1966-프린터 큐 ( https://www.acmicpc.net/problem/1966 )

# 배운점:
# 0) 특정 인덱스 값이 몇 번째로 pop이 되는지 체크하는 방법으로써는 visited를 이용하면됨
M = 1   # 특정 인덱스 값

q = list(map(int, input().split())) # 프린트 큐 중요도 값
visited = [False] * len(q)
q[M] = True

# =============================================================== #




