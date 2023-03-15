import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())  # 노트북
note = [[0] * M for _ in range(N)]  # 노트북
# paper = [[0] * 12 for _ in range(12)]

R, C = 0, 0


# ========================================
# 1) 스티커 붙이기 가능한 모눈종이 공간인지 확인
# ========================================
def pastable(x, y):
    global note

    # 1-1) 특정 영역에 붙일 수 있는가 확인하는 작업
    for i in range(R):
        for j in range(C):
            # 모눈종이에 스티커가 있고 노트북 그 자리에도 이미 스티커가 있는 경우
            if note[x + i][y + i] == 1 and paper[i][j] == 1:
                return False

    # 1-2) 실제로 붙이는 작업
    for i in range(R):
        for j in range(C):
            if paper[i][j] == 1:
                note[x + i][y + j] = 1

    print('>>> after')
    for row in note:
        print(*row)

    return True


# ====================================
# 2) 스티커 붙이기 가능한 모눈종이 공간인지 확인
# ====================================
# B[x][y] = A[3-1-y][x] ==> 90도 회전


def rotate():
    global R, C
    global paper

    if R == 2 or 5 and C == 2 or 5:
        print('======>> BEFORE << =========')
        for row in paper:
            print(*row)
    # tmp는 R과 C가 바뀌는 경우에 대해서도 IndexError없이 처리해야 한다.
    tmp = [[0] * 12 for _ in range(12)]

    # tmp에 복사
    for i in range(R):
        for j in range(C):
            tmp[i][j] = paper[i][j]

    # 90도 회전하여 paper에 저장
    paper = [[0] * R for _ in range(C)]
    for i in range(C):
        for j in range(R):
            paper[i][j] = tmp[R - 1 - j][i]

    # 90도 회전하면 가로와 세로가 뒤바뀐다.
    R, C = C, R

    if R == 2 or 5 and C == 2 or 5:
        print('======>> AFTER ROTATE << =========')
        for row in paper:
            print(*row)


# 로직 시작
for _ in range(K):
    R, C = map(int, input().split())  # 스티커가 인쇄된 모눈종이
    paper = [list(map(int, input().split())) for _ in range(R)]  # 스티커 영역

    for rot in range(4):    # 회전 방향은 0, 1, 2, 3
        is_paste = False  # 스티커 붙였는지 여부 초기화
        for x in range(N - R):  # 노트북 가로길이 - 스티커 가로 길이
            if is_paste:
                break
            for y in range(M - C):  # 노트북 세로길이 - 스티커 세로 길이
                if pastable(x, y):  # 세로이동 -> 끝까지가면 가로이동 -> 붙일 수 있는지 체크
                    is_paste = True
                    break
        if is_paste:
            break

        # 가로세로 모두 못 붙인다면 회전
        rotate()

cnt = 0

for i in range(N):
    for j in range(M):
        cnt += note[i][j]

print(cnt)
