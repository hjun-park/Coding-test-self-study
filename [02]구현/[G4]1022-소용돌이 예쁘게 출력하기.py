import sys

input = sys.stdin.readline

'''
    참고: https://hooongs.tistory.com/255
'''

# 반시계방향 선언
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

r1, c1, r2, c2 = map(int, input().split())

board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]  # 출력할 보드
number_of_board = (c2 - c1 + 1) * (r2 - r1 + 1)  # 출력할 보드 가로세로 사이즈

x = y = 0
num = 1
cnt = 0  # 한 방향에서 움직이는 횟수
dcnt = 1  # 한 방향에서 움직어야할 횟수 (cnt가 좌, 우를 가리키는 경우 1을 증가)
d = 0

while number_of_board > 0:  # 출력보드에 모든 값이 써질 때까지 시행
    if r1 <= x <= r2 and c1 <= y <= c2:  # 출력보드 사이즈 범위 안이라면
        number_of_board -= 1  # 출력보드에 쓸 것이므로 사이즈 -1
        board[x - r1][y - c1] = num  # 출력 보드에 num값을 대입
        max_num = num  # max_num을 num으로 설정 - 나중에 예쁘게 출력 위함(공백)

    # 이동 카운트와 num 증가
    num += 1
    cnt += 1

    # 방향 이동
    x = x + dx[d]
    y = y + dy[d]

    # 한 번 앞으로 이동하고 방향전환이 필요한지 여부 체크
    if cnt == dcnt:
        cnt = 0  # cnt를 0으로 초기화
        d = (d + 1) % 4  # 방향 전환
        if d == 0 or d == 2:  # 왼쪽 혹은 오른쪽 방향을 이동할 땐 이동횟수가 증가
            dcnt += 1

# 가장 큰 수에서 1을 빼줌 ( 소용돌이 끝을 고려 )
max_num_len = len(str(max_num - 1))
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(board[i][j]).rjust(max_num_len), end=' ')
    print()
