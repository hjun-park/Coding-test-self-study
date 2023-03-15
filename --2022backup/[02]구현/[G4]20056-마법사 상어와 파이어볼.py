import sys
from collections import deque

input = sys.stdin.readline

''' 문제 
# NxN 파이어볼 M
# i번 파이어볼 위치: (r, c) 질량 m / 방향 d / 속력 s

# 특이사항
# 1번부터 번호가 매겨짐
# 열과 행 모두 끝끼리 묶여 있다 => 나머지연산 이용하자
# 같은 칸에 여러 파이어볼이 있을 수 있다.

# 파이어볼
# 1. 모든 파이어볼은 d의 방향으로 속력 s칸만큼 이동
# 2. 이동 후 파이어볼이 2개 이상인 경우
#  -> 같은 칸에 있는 파이어볼은 모두 하나로
#  -> 파이어볼은 4개의 파이어볼로 나누어짐
#      -> 나누어졌을 때 질량, 속도, 방향은 일정한 공식으로 변환된다. (문제 참고)
# 3. 질량이 0인 파이어볼은 소멸되어 없어진다.
'''

N, M, K = map(int, input().split())
graph = [[deque() for _ in range(N)] for _ in range(N)]

moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def move_fireball():
    # -> 문제점: (1, 2) -> (2, 4) 이동했는데 순서대로 훑기 때문에
    # 변경사항이 그 이후 좌표로 반영된 상태에서 또 훑게 된다.
    # -> 해결방법: copy를 이용하거나 새로운 배열에 저장한다.
    copied_graph = [[deque() for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            while graph[x][y]:
                m, s, d = graph[x][y].pop()

                nx = (x + moves[d][0] * s) % N
                ny = (y + moves[d][1] * s) % N

                # print(f'{(x, y)} => {s}속력, {d}방향 => {(nx, ny)}')

                copied_graph[nx][ny].append((m, s, d))

    return copied_graph


def merge_fireball(x, y, size):
    dir_list = []
    new_m, new_s, new_d = 0, 0, []
    # 같은 칸에 있는 파이어볼은 어떻게 하나로 합치지 ?
    while graph[x][y]:
        m, s, d = graph[x][y].pop()
        new_m += m
        new_s += s
        dir_list.append(d)

    new_m = new_m // 5

    # 질량 0인 파이어볼은 소멸되어 없어진다.
    if new_m == 0:
        return

    new_s = new_s // size

    # 짝수/홀수 끼리 모였는지 확인
    eo_list = [x % 2 for x in dir_list]

    # 짝수 혹은 홀수만 모여있다면
    if sum(eo_list) == len(dir_list) or sum(eo_list) == 0:
        new_d = [0, 2, 4, 6]
    else:
        new_d = [1, 3, 5, 7]

    for n in range(4):
        graph[x][y].append((new_m, new_s, new_d[n]))

    # 짝수 혹은 홀수는 플래그로도 가능
    # if nm != 0:
    #     for idx in range(4):
    #         nd = 2 * idx if flag == 0 else 2 * idx + 1
    #         a[i][j].append([nm, ns, nd])


for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r - 1][c - 1].append((m, s, d))

# for row in graph:
#     print(*row)

# K번 명령
for k in range(K):
    graph = move_fireball()

    # 2개 이상이 있는 경우
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 2:
                merge_fireball(i, j, len(graph[i][j]))

    # print(f"# ================ {k + 1}번째 명령 후")
    # for row in graph:
    #     print(*row)
    # print()

# 남아 있는 파이어볼 질량 합 구하기
result = 0
for i in range(N):
    for j in range(N):
        while graph[i][j]:
            m, s, d = graph[i][j].pop()
            result += m

print(result)
