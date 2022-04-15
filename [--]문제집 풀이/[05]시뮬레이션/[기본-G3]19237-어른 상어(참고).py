from sys import stdin


SHARK, SCENT = 0, 1


def visitable(r, c):
    return 0 <= r < N and 0 <= c < N


def simulation():
    # 냄새 뿌리기.
    for s_idx, values in enumerate(sharks):
        if values is None:
            continue

        r, c, _ = values
        # 냄새를 뿌릴 수 있는 경우.

        print(r, c, SHARK)
        exit(0)
        if board[r][c] is None or board[r][c][SHARK] == s_idx:
            board[r][c] = [s_idx, K]
        else:
            sharks[s_idx] = None

    # 상어 이동
    for s_idx, values in enumerate(sharks):
        if values is None:
            continue

        r, c, cur_dir = values
        # 빈칸으로 이동 가능한 경우
        for next_dir in priority[s_idx][cur_dir]:
            dr, dc = dirs[next_dir]
            next_r, next_c = r + dr, c + dc

            if visitable(next_r, next_c) and board[next_r][next_c] is None:
                sharks[s_idx] = [next_r, next_c, next_dir]
                break
        # 자신의 냄새가 있는 칸으로 이동 가능한 경우
        else:
            for next_dir in priority[s_idx][cur_dir]:
                dr, dc = dirs[next_dir]
                next_r, next_c = r + dr, c + dc

                if visitable(next_r, next_c) and board[next_r][next_c][SHARK] == s_idx:
                    sharks[s_idx] = [next_r, next_c, next_dir]
                    break
            # 위의 2가지가 아니라면 이동 불가.
            else:
                sharks[s_idx] = None

    # 냄새 감소
    for r in range(N):
        for c in range(N):
            if board[r][c] is None:
                continue

            board[r][c][SCENT] -= 1

            if board[r][c][SCENT] == 0:
                board[r][c] = None


if __name__ == "__main__":
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    N, M, K = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for _ in range(N)]
    cur_shark_dirs = list(map(int, stdin.readline().split()))  # 각 상어의 방향
    sharks = [0] * M

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                # 위치, 방향을 인덱스에 맞게 감소
                sharks[board[i][j] - 1] = [i, j, cur_shark_dirs[board[i][j] - 1] - 1]
                board[i][j] -= 1
            board[i][j] = None

    priority = [[[0] for _ in range(4)] for _ in range(M)]

    for shark_idx in range(M):
        for p_idx in range(4):
            # 우선 순위 방향을 dirs 인덱스에 맞게 감소
            priority[shark_idx][p_idx] = [p - 1 for p in list(map(int, stdin.readline().split()))]

    print(board)
    print(sharks)
    for cur_time in range(-1, 1001):
        # 1번 상어만 남는 경우
        if sharks.count(None) == M - 1:
            print(cur_time)
            exit(0)
        else:
            simulation()
    else:
        print(-1)
