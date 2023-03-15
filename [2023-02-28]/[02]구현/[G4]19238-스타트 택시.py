import sys
from collections import deque

input = sys.stdin.readline

N, M, FUEL = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
start_x, start_y = map(int, input().split())
p_list = [list(map(int, input().split())) for _ in range(M)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

'''
    https://tmdrl5779.tistory.com/m/153?category=831693
    - 이동 시마다 연료를 -= 1 하는 것이 아니라 이동거리를 구하고 연료를 뺀다.
    
    1) BFS를 이용하여 최단 거리에 있는 사람을 찾고 그 거리를 저장한다.
    2) 사람을 태우고 목적지까지 다시 BFS를 이용하여 거리를 저장한다.
    3) 만약 사람 혹은 목적지까지 도달할 수 없다면 -1 출력 후 종료
    4) 도달할수 있다면
     4-1) 연료에서 1) 거리만큼 연료를 뻈을 때 음수라면 -1 출력 
     4-2) 연료에서 1) 빼도 양수라면 2)를 빼보고 음수라면 종료하고 -1 출력 
     4-3) 종료가 안됐으면 연료에 2번 * 2
    5) 모든 사람 태운 후 남은 연료 확인
'''


def bfs(start_x, start_y):
    # 이동거리는 visited 이용하여 셀 수 있다.
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 내에 속하고 벽도 아니며 거리가 안 정해져있다면
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1  # visited 갱신방법
                    q.append((nx, ny))

    return visited  # 최단거리가 기록된 배열을 반환해준다.


def check_short_distance(visited: list, p_list: list):
    i = 0
    if len(p_list[0]) == 4:
        for x1, y1, x2, y2 in p_list:
            p_list[i].append(visited[x1 - 1][y1 - 1])
            i += 1

        p_list.sort(key=lambda x: (-x[4], -x[0], -x[1]))


def logic(sx, sy):
    global FUEL

    while p_list:
        # 1) 매 이동 시마다 최단거리에 있는 사람을 찾고 그 거리를 저장한다.
        visited = bfs(sx - 1, sy - 1)
        check_short_distance(visited, p_list)

        # 2) 사람을 태우고 목적지까지 다시 BFS를 이용하여 거리를 저장한다.
        x1, y1, x2, y2, dist = p_list.pop()

        # 이동 후에 최단거리를 다시 구해야하기 때문에 최단거리값 다시 제거
        for p in p_list:
            p.pop()

        # 여기서 핵심은 택시시작 -> 사람위치, 사람위치 -> 목적지
        # 해당하는 BFS 2개를 만든게 아니라,
        # 기존 BFS를 2개 쓰고 BFS거리가 계산되어있는 visited를 인자로 넘겨줌
        visited = bfs(x1 - 1, y1 - 1)  # 택시시작점 -> 사람 위치
        dist2 = visited[x2 - 1][y2 - 1]  # 사람 위치 -> 목적지

        # 목적지 이동
        sx, sy = x2, y2

        # 3) 만약 승객(dist) 혹은 목적지(dist2)까지 도달할 수 없다면 -1 출력 후 종료
        if dist == -1 or dist2 == -1:
            print(-1)
            return

        # 4) 도달할수 있다면
        #  4-1) 연료에서 1) 거리(dist)만큼 연료를 뻈을 때 음수라면 -1 출력 후
        FUEL -= dist
        if FUEL < 0:
            print(-1)
            return

        #  4-2) 연료에서 1) 빼도 양수라면 2)(dist2)를 빼보고 음수라면 종료하고 -1 출력 종료
        FUEL -= dist2
        if FUEL < 0:
            print(-1)
            return

        #  4-3) 종료가 안됐으면 연료에 2번 * 2
        FUEL += dist2 * 2

    # 5) 모든 사람 태운 후 남은 연료 확인
    if FUEL < 0:
        print(-1)
    else:
        print(FUEL)


logic(start_x, start_y)
