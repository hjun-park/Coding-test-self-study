import sys
from collections import deque
import heapq

input = sys.stdin.readline

'''
    참고: https://inspirit941.tistory.com/207
'''

N = int(input())
graph = []
q = deque()

# 상좌하우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
time = 0
size = 2
already_eat = 0

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] == 9:
            start = (i, j, 0)
            q.append(start)
            graph[i][j] = 0  # 시작 위치 값을 0으로 바꿈


def bfs():
    min_dist = []  # heapq
    visited = set()
    while q:
        x, y, cnt = q.popleft()
        visited.add((x, y))

        # for d in range(4):
        for dx, dy in dirs:
            # nx = x + dx[d]
            # ny = y + dy[d]
            nx = x + dx
            ny = y + dy

            # 범위 내이며 방문을 안 한 경우
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))

                # [이동가능] 다음 이동지역이 상어크기와 같거나 0인 경우
                if graph[nx][ny] == 0 or graph[nx][ny] == size:
                    q.append((nx, ny, cnt + 1))
                    continue

                # [이동불가] 다음 이동지역이 상어크기보다 큰 경우
                if graph[nx][ny] > size:
                    continue

                # [먹는 경우] 상어 크기보다 작은 경우
                else:
                    # cnt를 기준으로 heapq 정렬
                    heapq.heappush(min_dist, (cnt + 1, nx, ny))

    # 먹을 수 있는게 있다면 먼저 먹을 걸 return
    if min_dist:
        return min_dist[0]
    else:
        return None


while True:
    next_value = bfs()

    # 만약 먹을 물고기가 없으면 엄마 상어한테 도움 요청
    if next_value is None:
        break

    # 먹을 물고기가 있는 경우 다음 물고기를 먹기까지 걸린 시간 계산
    cnt, nx, ny = next_value
    time += cnt

    # 먹은 물고기 개수를 센다.
    already_eat += 1

    # 만약 현재 크기만큼 먹었으면 물고기 개수를 초기화 하고 크기를 증가시킨다.
    if already_eat == size:
        size += 1
        already_eat = 0

    # 다음 출발점을 넣는다. (물고기 위치)
    # 물고기를 잡아먹었으니 0으로 변경한다.
    q.append((nx, ny, 0))
    graph[nx][ny] = 0

print(time)
