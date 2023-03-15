import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

'''
    생각해 볼 요소 (https://bladejun.tistory.com/138?category=426398)
    1) 언제 어떻게 회전을 해 주었는가?
     - (N, N)이 최종 목적지이므로 오른쪽, 그리고 아래로만 회전이 돌아가도록 한다.
     - 가로 -> 세로 회전 시 각 드론위치1, 드론위치2를 축으로 해서 아래로 회전하도록 함
     - 세로 -> 가로 회전 시 각 드론위치1, 드론위치2를 축으로 해서 오른쪽으로 회전하도록 함
      
    2) visited 체크를 set으로 한 이유 ?
     -> 시간복잡도를 줄이기 위해서,
     -> 드론이 2개의 좌표를 잡아먹기 때문에 2차원 배열로 하기에는 시간복잡도가 많이 나올 것 같다.
     
    3) BFS 돌 때 queue에는 무엇을 넣어주었는가 ?
     -> 드론위치1, 드론위치2, 시간  
 
'''


def check_move(pos1, pos2, copied_graph):
    x, y = 0, 1  # pos1의 x, y좌표 표현을 pos[0] ,pos[1] 해야하는데 이를 눈으로 보기 쉽게 표현
    moves = []

    # 3-1) [좌우상하] 이동 가능여부 체크
    for d in range(4):
        n_pos1 = (pos1[x] + dx[d], pos1[y] + dy[d])
        n_pos2 = (pos2[x] + dx[d], pos2[y] + dy[d])

        # 상하좌우로 이동할 시 드론 좌표 모두 이동 가능한 경우 moves에 추가
        if copied_graph[n_pos1[x]][n_pos1[y]] == 0 and copied_graph[n_pos2[x]][n_pos2[y]] == 0:
            moves.append((n_pos1, n_pos2))

    # 3-2) [회전] 회전해서 이동 가능한 경우라면 추가
    if pos1[x] == pos2[x]:  # x좌표가 같은 선상이면 드론은 가로방향
        UP, DOWN = -1, 1  # 마찬가지로 보기 편하게
        for d in [UP, DOWN]:  # 위 아래로 확인
            # 만약 회전이 가능하다면 ( 드론이 (1,1)(1,2) 를 차지한다면 다음 행만 확인해도 된다. (2,1)(2,2))
            if copied_graph[pos1[x] + d][pos1[y]] == 0 and copied_graph[pos2[x] + d][pos2[y]] == 0:
                # 회전이 가능할 시 드론위치1, 2를 축으로 회전한 결과인 각 드론 위치1, 드론 위치2 아래 좌표를 추가한다.
                moves.append((pos1, (pos1[x] + d, pos1[y])))
                moves.append((pos2, (pos2[x] + d, pos2[y])))

    else:  # y 좌표가 같은 선상이면 드론은 세로방향
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if copied_graph[pos1[x]][pos1[y] + d] == 0 and copied_graph[pos2[x]][pos2[y] + d] == 0:
                moves.append(((pos1[x], pos1[y] + d), pos1))  # pos1을 축으로 왼쪽/오른쪽으로 돌림
                moves.append(((pos2[x], pos2[y] + d), pos2))  # pos2을 축으로 왼쪽/오른쪽으로 돌림

    return moves


def solution(board):
    N = len(board)

    # 1) 시작지가 (1, 1)니까 테두리가 전부 1인 copied_graph 라는 그래프 따로 생성
    copied_board = [[1] * (N + 2) for _ in range(N + 2)]

    for i in range(N):
        for j in range(N):
            copied_board[i + 1][j + 1] = board[i][j]

    q = deque()
    q.append(((1, 1), (1, 2), 0))  # 드론 1좌표, 드론 2좌표, 시간
    visited = set([((1, 1), (1, 2))])  # 시간복잡도를 줄이기 위해 set 사용

    # 2) BFS 순환
    while q:
        pos1, pos2, time = q.popleft()

        # 2-1) 드론의 한 부분이라도 (N, N) 도달 시에는 시간 반환
        if pos1 == (N, N) or pos2 == (N, N):
            return time

        # 3) 방문할 수 있는 모든 경우를 체크
        moves = check_move(pos1, pos2, copied_board)

        # 4) 방문 시행 후 이동이 가능하다면 queue에 추가하고 드론좌표1, 2를 tuple로 묶어 방문처리한다.
        for next_pos in moves:  # moves는 이동 가능한 좌표
            if next_pos not in visited:  # 방문하지 않았다면 q에 집어넣기
                q.append((next_pos[0], next_pos[1], time + 1))
                visited.add(next_pos)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
