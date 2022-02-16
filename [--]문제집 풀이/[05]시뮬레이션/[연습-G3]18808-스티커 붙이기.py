import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())  # 노트북
note = [[0] * M for _ in range(N)]  # 노트북
R, C = 0, 0

# ====================================
# 1) 스티커 붙이기 가능한 모눈종이 공간인지 확인
# ====================================
def pastable(x, y):
    # 1-1) 특정 영역에 붙일 수 있는가 확인하는 작업
    for i in range(R):
        for j in range(C):
            # 모눈종이에 스티커가 있고 노트북 그 자리에도 이미 스티커가 있는 경우
            if paper[x + i][y + i] == 1 and note[i][j] == 1:
                return False

    # 1-2) 실제로 붙이는 작업
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1:
                note[x + i][y + i] = 1

    return True


# ====================================
# 2) 스티커 붙이기 가능한 모눈종이 공간인지 확인
# ====================================
# B[x][y] = A[3-1-y][x] ==> 90도 회전
def rotate():
    global R, C
    tmp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            tmp[i][j] = paper[i][j]

    for i in range(C):
        for j in range(R):
            paper[i][j] = tmp[R - 1 - j][i]

    # 90도 회전하면 가로와 세로가 뒤바뀐다.
    R, C = C, R


for _ in range(K):
    R, C = map(int, input().split())  # 스티커가 인쇄된 모눈종이
    paper = [list(map(int, input().spit())) for _ in range(R)]  # 스티커 영역

    for rot in range(4):
        is_paste = False
        for x in range(N):
            for y in range(M):





