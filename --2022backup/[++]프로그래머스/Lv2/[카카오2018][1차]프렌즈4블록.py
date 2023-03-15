'''
[문제이해]
1. 2x2 4개 같은 블록 -> 터뜨리면서 점수
2. 여러 2x2에 같은 블록이 존재할 수 있다. -> 터뜨리기 전 check는 복사해서 하자
3. 입력으로 블록이 주어졌을 때 총 지워지는 개수 return

[구현함수 파악]
1. 보드가 주어지면 터지는 블록 개수 return

[프로세스]
1. 2x2 블록 체크 -> 내용변경('.')
2. 변경된 내용만 터뜨리고 cnt증가
3. 블록들을 아래로 떨어트리기 (세부로직 필요)
4. 다시 1번부터 반복한다.

[수도코딩 /손코딩]
# 블록을 체크하고 2x2 영역을 ('.') 변경하는 알고리즘
board를 복사한 copied_board 생성
is_crash = False
for i in range(N-1):
    for j in range(M-1):
        if ('.')가 아니면서 4구역이 모두 같다면: # (set(len)이용하자) board에서체크
            if 이미 해당 구역이 '.'라면 중복, cnt -= 1  // copied_board에서 체크
            복사한 board에서 4구역 모두 ('.')로 변경
            is_crash = True
            cnt += 4

# 블록을 아래로 떨어트리는 과정
# 끝에서부터 시작해서, 투포인터 잡아주기
def down():
    for x in range(M):
        for y in range(N-1, -1, -1):
            for z in range(N-1, y, -1):
                if board[y][x] != '.' and board[z][x] == '.'    # 위 블록, 아래는 빈 공간
                    graph[z][x], graph[y][x] = graph[y][x], graph[z][x] # 두 공간 위치를 바꾸어 줌
                    break

'''

from copy import deepcopy


def down(N, M, board):
    for x in range(M):
        for y in range(N - 1, -1, -1):
            for z in range(N - 1, y, -1):
                if board[y][x] != '.' and board[z][x] == '.':  # 위 블록, 아래는 빈 공간
                    board[z][x], board[y][x] = board[y][x], board[z][x]  # 두 공간 위치를 바꾸어 줌
                    break
    return board


# 조금 더 쉬운 동작
def easy_down(N, M, x2):
    # [블록이 중력을 받아 down 되는 동작]
    for _ in range(N):
        for i in range(M - 1):  # 첫 번재 행부터 마지막-1번째 행 전까지 진행
            for j in range(N):
                if x2[i + 1][j] == '.':  # 다음 행이 .이라면 서로 교체
                    x2[i + 1][j], x2[i][j] = x2[i][j], '.'


def solution(m, n, board):
    N, M = m, n
    for i in range(N):
        board[i] = list(board[i])

    for row in board:
        print(*row)

    # 블록 체크 후 2x2 사이즈 터뜨리기
    # board를 복사한 copied_board 생성
    cnt = 0
    while True:
        copied_board = deepcopy(board)
        is_crash = False
        for i in range(N - 1):
            for j in range(M - 1):
                temp = [board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]]
                if board[i][j] != '.' and len(set(temp)) == 1:
                    for k in range(i, i + 2):
                        for l in range(j, j + 2):
                            if copied_board[k][l] == '.':
                                cnt -= 1
                                continue
                            copied_board[k][l] = '.'
                            is_crash = True
                    cnt += 4

        # 터진 블록 여부 체크(없다면 break)
        if not is_crash:
            break

        # 블록을 조정하기
        board = down(N, M, copied_board)

    return cnt


# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
