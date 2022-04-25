'''
 S - 직진
 L - 좌회전
 R - 우회전
 격자끝 - 반대쪽 끝 ((1, 2) -> (-1, 2) 즉, (끝행, 같은 열))
 사이클: 빛이 이동하는 순환 경로
 데이터 - 문자열 길이는 일정

 [핵심]
 1. visited[x][y][k] : (현재 x,y 좌표에서 k의 방향으로 나감)

 [참고] https://studyandwrite.tistory.com/435
'''

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def route(grid, visited, x, y, k):
    N, M = len(grid), len(grid[0])

    # 방문처리 지정
    visited[x][y][k] = True
    # 다음 격자 지정
    nx = (x + dx[k]) % N
    ny = (y + dy[k]) % M
    # 사이클 길이 카운트
    cnt = 1

    # 방향 전환 후 이동
    while True:
        # 다음 격자 글씨에 따른 방향 전환
        if grid[nx][ny] == 'S':
            pass
        elif grid[nx][ny] == 'L':
            k = (k - 1) % 4
        elif grid[nx][ny] == 'R':
            k = (k + 1) % 4

        # 이동
        if not visited[nx][ny][k]:
            cnt += 1
            # 꼭 먼저 방문 처리 후 nx, ny를 재설정 해야 한다.
            visited[nx][ny][k] = True
            nx = (nx + dx[k]) % N
            ny = (ny + dy[k]) % M

            # 여기에 방문처리를 두면 이미 nx, ny 재설정 후에 두는 것이므로 원하는 값이 안 나온다.
            # visited[nx][ny][k] = True

        else:  # 반복되는 사이클을 만난 경우
            return cnt


def solution(grid):
    N, M = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    answer = []

    # 모든 격자와 각 격자의 4방향에 빛을 쏜다.
    for x in range(N):
        for y in range(M):
            for k in range(4):
                if not visited[x][y][k]:
                    answer.append(route(grid, visited, x, y, k))

    return sorted(answer)


print(solution(["SL", "LR"]))
