import sys
from collections import deque

input = sys.stdin.readline

'''
    # https://dirmathfl.tistory.com/383

    # 행렬에서 위로 읽기 위한 방법 (rotate 함수)
    # deepcopy 안 쓰고 temp_graph 이용을 해서 표현 가능
    # Answer 2: 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 로직 도는 방법
'''


def rotate(pos, l):  # pos: 현재 위치, l: 격자 크기
    cur_x, cur_y = pos

    '''
    예를 들어 격자에 값이 다음과 같다면,
    1 2             3 1
    3 4             4 2
    ↑로 읽고         →로 쓰면 된다.
    90도 회전
    '''
    for x in range(l):
        for y in range(l):
            # read ↑ (위로 읽는다)
            # 격자의 크기가 2일 때 (L=2)
            # 위로 읽을 때 x좌표 변화 ( 1 -> 0 -> 1 -> 0 ) :: x좌표와 격자 크기를 더하고 y와 1을 뺀다.
            # 위로 읽을 때 y좌표 변화 ( 0 -> 0 -> 1 -> 1 ) :: x좌표 따라서 증가값이 변한다.
            temp[x][y] = board[cur_x + l - 1 - y][cur_y + x]

    for x in range(l):
        for y in range(l):
            # write →
            # 현재 좌표를 기준으로 그냥 쓰면 된다.
            board[cur_x + x][cur_y + y] = temp[x][y]


def simulation(l):  # l: 격자 크기 ( 2, 4, 8 ... )
    # 1-1) 격자 크기(2, 4, 8 ...) 만큼 루프를 돈다. 돌면서 90도 회전 한다.
    for r in range(0, N, l):
        for c in range(0, N, l):
            rotate((r, c), l)

    check = [[0 for _ in range(N)] for _ in range(N)]

    # 2-1) 인접한 얼음이 3개 미만인 경우를 찾는다.
    for r in range(N):
        for c in range(N):
            if not board[r][c]:  # 얼음이 없는 경우라면 패스
                continue

            adj_cnt = 0  # 인접한 얼음 개수
            for d in range(4):
                next_r = r + dr[d]
                next_c = c + dc[d]

                # 인접한 곳에 얼음이 있다면 count 증가
                if 0 <= next_r < N and 0 <= next_c < N:
                    if board[next_r][next_c]:
                        adj_cnt += 1

            # check하지 않고 바로 녹이게 되면 탐색에 영향을 받음
            # 그래서 check 에다가 1로 체크한다.
            check[r][c] = 1 if adj_cnt < 3 else 0

    # 2-2) 찾은 얼음 녹이기
    for r in range(N):
        for c in range(N):
            if check[r][c]:  # 만약 check가 1이라면 얼음을 녹이는 대상이다.
                board[r][c] -= 1  # 얼음을 녹인다.


# 백준: 4963 섬의 개수와 같은 로직
def bfs(start):
    q = deque([start])
    cnt = 1

    while q:
        cur_r, cur_c = q.popleft()
        for d in range(4):
            next_r = cur_r + dr[d]
            next_c = cur_c + dc[d]

            if 0 <= next_r < N and 0 <= next_c < N:
                if board[next_r][next_c] and not visited[next_r][next_c]:
                    visited[next_r][next_c] = 1
                    q.append((next_r, next_c))
                    cnt += 1

    return cnt


if __name__ == '__main__':
    N, Q = map(int, input().split())
    N = 2 ** N  # N은 문제에서 안 쓰이고 제곱이 쓰임
    board = [list(map(int, input().split())) for _ in range(N)]

    L = list(map(int, input().split()))
    max_l = max(L)

    # 분리된 격자를 임시로 담아두기 위함
    temp = [[0 for _ in range(2 ** max_l)] for _ in range(2 ** max_l)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]

    # 1) 2^N x 2^N 나눈다.
    for cur_l in L:
        simulation(2 ** cur_l)

    # Asnwer 1: 남아 있는 얼음의 총합
    sum_ice = sum(sum(board, []))
    print(sum_ice)

    # Answer 2: 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
    max_ice = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] and not visited[i][j]:
                visited[i][j] = 1
                max_ice = max(max_ice, bfs((i, j)))

    print(max_ice)
