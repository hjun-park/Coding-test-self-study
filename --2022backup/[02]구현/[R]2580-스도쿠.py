import sys

input = sys.stdin.readline

'''
 [https://paris-in-the-rain.tistory.com/90]
    1. count 체크하기
    1-1. count가 해당 리스트 길이만큼 왔다면 조사를 다 한 것이므로 출력하고 종료
    1-2. count가 길이만큼 도달하지 못했다면
     - 0인 좌표를 하나 가져와서 해당 좌표가 들어갈 수 있는 함수 탐색 (2)
    
    2. numbers 생성
    2-1. [행열에 대한 체크] 9번을 순회하면서 
      (행) 해당 좌표의 숫자가 numbers에 있다면 numbers에 대해서 제거
      (열) 해당 좌표의 숫자가 numbers에 있다면 numbers에 대해서 제거
    
    2-2. [3x3에 대한 체크] 
      - 3을 나머지버림으로 몫 계산
      - 행열을 체크하는데, 시작은 x*3, 끝은 (x+1)*3  
      - 해당 위치가 numbers에 있다면 해당 값을 numbers에서 제거
    - 결과적으로 numbers 반환 
    
    3. 반환된 결과를 받아서 해당 값은 graph의 값으로 셋팅,
      만약에 dfs를 끝까지 돌지 못하고 나왔다면 백트래킹에 의해 해당 값은 0으로 복구하기
'''

# board = [list(map(int, input().split())) for _ in range(9)]
# # 스도쿠에서 채워넣어줘야 할 (값이 0인 좌표) 위치
# emptySpace = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
#
#
# def candidating(x, y):  # 해당 좌표에 대해서 유효성 검증
#     numbers = [i + 1 for i in range(9)]
#
#     for k in range(9):
#         if board[x][k] in numbers:
#             numbers.remove(board[x][k])
#         if board[k][y] in numbers:
#             numbers.remove(board[k][y])
#
#     x //= 3
#     y //= 3
#     for i in range(x * 3, (x + 1) * 3):
#         for j in range(y * 3, (y + 1) * 3):
#             if board[i][j] in numbers:
#                 numbers.remove(board[i][j])
#     return numbers
#
#
# def dfs(count):
#     if count == len(emptySpace):
#         for row in board:
#             print(*row)
#         return
#
#     (i, j) = emptySpace[count]
#     candi = candidating(i, j)
#     for num in candi:
#         board[i][j] = num
#         dfs(count + 1)
#         board[i][j] = 0  # 복구
#
#
# dfs(0)  # count: 스도쿠에서 빼낸 숫자


def dfs(depth):
    if depth == blank_num:
        for v in board:
            print(' '.join(map(str, v)))
        exit(0)

    y, x = pos[depth]
    for n in range(1, 10):
        if not row_arr[y][n] and not col_arr[x][n] and not box_arr[y // 3 * 3 + x // 3][n]:
            row_arr[y][n] = col_arr[x][n] = box_arr[y // 3 * 3 + x // 3][n] = True
            board[y][x] = n
            dfs(depth + 1)
            row_arr[y][n] = col_arr[x][n] = box_arr[y // 3 * 3 + x // 3][n] = False
            board[y][x] = 0


board = [list(map(int, input().split())) for _ in range(9)]
row_arr = [[False] * 10 for _ in range(10)]
col_arr = [[False] * 10 for _ in range(10)]
box_arr = [[False] * 10 for _ in range(10)]

pos = []
for r in range(9):
    for c in range(9):
        if not board[r][c]: # 빈 자리 (0) 가 아닐 경우에
            pos.append([r, c])  # pos에 해당 좌표 추가
        else:
            row_arr[r][board[r][c]] = True      # 행(좌우) 체크
            col_arr[c][board[r][c]] = True      # 열(상하) 체크
            box_arr[r // 3 * 3 + c // 3][board[r][c]] = True    # 대각선 체크

blank_num = len(pos)
dfs(0)
