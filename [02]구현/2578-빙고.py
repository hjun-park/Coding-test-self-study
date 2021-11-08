import sys

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
bingo = [list(map(int, input().split())) for _ in range(5)]

visited = [[False] * 5 for _ in range(5)]


def check():
    # 가로 체크
    cnt = 0
    for x in range(5):
        row_flag = True
        if False in visited[x]:  # 빙고가 아니라면
            row_flag = False
        if row_flag:
            cnt += 1

    # 세로 체크
    for y in range(5):
        col_visited = list(map(list, zip(*visited)))
        col_flag = True
        if False in col_visited[y]:
            col_flag = False
        if col_flag:
            cnt += 1

    # 대각선 체크
    l_flag, r_flag = True, True
    for i in range(5):
        if not visited[i][i]:
            l_flag = False
        if not visited[i][4 - i]:
            r_flag = False

    if l_flag:
        cnt += 1
    if r_flag:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


count = 0
for x in bingo:
    while x:
        num = x.pop(0)
        count += 1
        for i in range(5):
            for j in range(5):
                if graph[i][j] == num:
                    visited[i][j] = True

        # 5번부터 1 bingo를 만들 수 있음, 그 때부터 빙고개수 체크
        if count >= 5 and check():
            print(count)
            sys.exit(0)
