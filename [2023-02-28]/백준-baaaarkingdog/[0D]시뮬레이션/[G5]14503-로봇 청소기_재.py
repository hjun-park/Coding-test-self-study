import sys

input = sys.stdin.readline

# ( 북 -> 동 -> 남 -> 서 )
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())  # 가로/세로
r, c, d = map(int, input().split())  # 로봇 x, y, 방향
graph = [list(map(int, input().split())) for _ in range(N)]  # 청소구역

# 1. 현재 위치 청소
graph[r][c] = 2
cnt = 1

# 2. 현재 위치에서 현재 방향 기준으로 왼쪽 방향부터 차례 탐색
while True:

    # 1. flag
    is_cleaned = False
    # 2. 네 방향 청소 가능한 지 확인
    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]

        if 0 <= nx < N and 0 <= ny < M:     # 범위 내이면서
            if graph[nx][ny] == 0:          # 청소하지 않았다면
                r, c = nx, ny               # 한 칸 전진하고
                graph[r][c] = 2             # 해당 칸 청소처리
                cnt += 1                    # 청소 횟수 증가
                is_cleaned = True           # 청소처리
                break                       # 청소했으니 다시 왼쪽부터 확인

    # 3. 만약 네 방향 모두 청소할 수 없는 곳이라면
    if not is_cleaned:
        # 1. 후진 방향 설정
        nx, ny = r - dx[d], c - dy[d]

        # 2. 후진하려는 방향이 벽이라면 종료
        if graph[nx][ny] == 1:
            print(cnt)
            break

        r, c = nx, ny


