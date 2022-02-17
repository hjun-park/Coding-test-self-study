import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
note = [[0] * M for _ in range(N)]


def rotate(paper):
    global R, C
    # 90도로 회전해 주는 함수
    '''
        ----------------------------
            1 2          5 3 1
            3 4     =>   6 4 2
            5 6
        ----------------------------

        a[0][0] => a[0][2]
        a[0][1] => a[1][2]
        a[2][0] => a[0][0]
        a[2][1] => a[1][0]

        -> 여기서 유추해 볼 수 있는 것
        a[x][y]  =>  a[행-1-y][x]

    '''

    # 충분한 사이즈의 tmp를 구함 (회전하면 사이즈 변경되므로)
    tmp = [[0] * 12 for _ in range(12)]

    # tmp에 스티커 복사
    # tmp = deepcopy(paper)
    for i in range(R):
        for j in range(C):
            tmp[i][j] = paper[i][j]

    # print(f">>>>>> 회전 전 {R} {C}")
    # for row in paper:
    #     print(*row)
    #
    # print(f'>>>>>> temp')
    # for row in tmp:
    #     print(*row)

    # R, C 스왑
    backup_row = R
    R, C = C, R

    # 새로운 스티커 종이 생성 (회전하면 사이즈 변경되므로)
    copied_paper = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            copied_paper[i][j] = tmp[backup_row - 1 - j][i]

    # print(f">>>>>> 회전 후 {R} {C}")
    # for row in copied_paper:
    #     print(*row)

    # print()
    # print()
    # print()

    return copied_paper


def pastable(x, y):  # x, y = 노트북에서 붙일 좌표의 시작점

    # 특정 영역에 붙일 수 있는지 확인
    for i in range(R):
        for j in range(C):
            if note[x + i][y + j] == 1 and paper[i][j] == 1:  # 스티커도 1 노트북도 1
                return False

    # 붙일 수 있다면 붙이기
    for i in range(R):
        for j in range(C):
            if paper[i][j] == 1:  # 스티커가 1인 부분은
                note[x + i][y + j] = 1  # 붙여주기

    return True


for _ in range(K):
    R, C = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(R)]

    for rot in range(4):  # 방향 회전은 0, 1, 2, 3  해서 총 4개
        is_paste = False  # 붙였는지 확인하는 변수 초기화

        # >> 1) 노트북 내에서 좌표 하나씩 움직이며 붙일 수 있는지 체크
        for i in range(N - R + 1):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!! +1을 안붙여줘서 못풀었음
            if is_paste:  # 행에서 붙였는지 체크하여서 조금 더 연산을 줄임
                break

            for j in range(M - C + 1):
                if pastable(i, j):  # 안 붙였으면 붙일 수 있는지 확인
                    is_paste = True  # 붙일 수 있는 경우 체크
                    break

        # >> 2) 스티커를 붙였는지 확인 붙였다면 회전할 필요 없다.
        if is_paste:
            break

        # >> 3) 노트북 모든 방향을 체크했음에 불구하고 없는 경우 전환
        paper = rotate(paper)

# >> 4) 다 끝나면 노트북에서 스티커가 붙은 칸을 출력
cnt = 0

for i in range(N):
    for j in range(M):
        cnt += note[i][j]

print(cnt)
