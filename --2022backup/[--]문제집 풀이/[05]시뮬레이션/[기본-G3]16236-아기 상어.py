import heapq
import sys
from collections import deque

input = sys.stdin.readline

'''
    [요약]
    1. 크기 N 물고기 M 아기상어 2 // 한 칸당 물고기 1마리
    2. 자기보다 큰 물고기 지나갈 수 없음
    3. 크기가 같은 경우는 지나갈 수 있음
    4. 자기보다 작은 물고기는 먹을 수 있음
    
    5. 상어 이동 방향 결정 방법
     5.1 [0] 공간에 먹을 수 있는 물고기 체크
     5.2 [1] 물고기 1마리라면 그거 먹으러 감
     5.3 [2이상] 물고기 > 1이라면 가장 가까운 물고기 잡으러 감
    
    6. [5.3에 대한 보충] 
     6.1. 거리란 물고기까지 갈 때 지나야 되는 최소 칸을 말함
     6.2. 거리에 가까운 물고기가 많다면 북 -> 서 -> 남 -> 동 순으로
     
    7. 아기상어가 크기가 2일 때 물고기 2마리 먹으면 크기가 3으로 증가
    
    8. 총 몇 초동안 잡아 먹을 수 있는지 확인 
     
    
    [풀이] 
    0. 입력받음, 물고기는 따로 좌표로 저장할 필요 없을듯 (x, y, int(1e9)) -> 세번째 인자는 거리
    1. while True 시작
     1.3 [2마리 이상]
       - 물고기 최소 경로 저장할 튜플 생성 min_dist = []  => 힙큐로 쓸 것
       - 다시 for문을 돌면서 물고기를 찾음
       - 물고기를 찾았다면 물고기의 크기를 체크 후 잡아먹을 수 있겠다면 BFS 순환
         - 다음 이동지역이 상어와 크기가 같거나 0인 경우 => 큐에만 추가
         - 1보다 크고 상어보다 작은 경우 => min_dist에 heapq로 집어넣어 준다.
         - 상어보다 큰 경우 : 그냥 continue
       - 그렇게 하고 while q 끝나면 min_dist의 첫 번째 좌표를 뱉어냄
    2. BFS 순환이 끝나면 잡아먹을 물고기 확인 (None이라면 끝냄) - min_dist[0]가 출력됨
    3. 잡아먹을 물고기가 있다면 cnt추가, 잡아먹은 물고기 추가
    4. 만약 잡아먹은 물고기가 자기 사이즈보다 크면 자기사이즈 증가 후 잡아먹은 물고기 개수 초기화
    5. 잡아먹은 물고기 좌표 [nx][ny]는 초기화, queue에는 다음 좌표와 depth 0을 집어넣고 시작
     
    
    [주의점]
    0. heapq를 이용하고 상좌우하로 탐색을 하도록 만들면
       같은 거리에서 잡아먹는 방향을 고민할 필요가 없다.
    1. 상어의 크기는 2다.

'''

# 상 좌 우 하
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()
start = 0


# 0) 상어의 위치를 찾음
def find_start_point():
    global start
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                start = (i, j, 0)

                # 상어 좌표 값은 9인데, 이는 물고기 크기와 혼동 우려 있으므로 0으로 수정
                graph[i][j] = 0

                return


def bfs(s):
    # 물고기 최소 경로 저장할 튜플 생성 min_dist = []  => 힙큐로 쓸 것
    q.append(s)
    min_dist = []
    visited = [[False] * N for _ in range(N)]
    visited[s[0]][s[1]] = True

    #  - 상어의 시작점에서 BFS를 순회
    while q:
        x, y, depth = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = True

                    # - 다음 이동지역이 상어와 크기가 같거나 0인 경우 => 큐에만 추가
                    if graph[nx][ny] == shark_size or graph[nx][ny] == 0:
                        # print(f'11 물고기 같거나 0임')
                        q.append((nx, ny, depth + 1))

                    # - 0보다 크고 상어보다 작은 경우 => min_dist에 heapq로 집어넣어 준다.
                    elif 0 < graph[nx][ny] < shark_size:
                        # print(f'33. 힙에 추가되는 데이터 {(depth + 1, nx, ny)}')
                        heapq.heappush(min_dist, (depth + 1, nx, ny))

                    #  - 상어보다 큰 경우 : 그냥 continue
                    else:
                        # print(f'22 물고기 큼')
                        continue

    # 먹을 수 있는게 있다면 먼저 먹을 걸 return
    # if min_dist:
    #     return min_dist[0]
    # else:
    #     return None
    return min_dist[0] if min_dist else None


find_start_point()

shark_size = 2
eat_fish = 0
time = 0

# 1. while True 시작
while True:
    next_pos = bfs(start)

    # 엄마 상어 도움 요청
    if next_pos is None:
        break

    cnt, px, py = next_pos
    #  3. 잡아먹을 물고기가 있다면 이동시간 추가, 잡아먹은 물고기 추가
    time += cnt
    eat_fish += 1

    #  4. 만약 잡아먹은 물고기 수 자기 사이즈보다 크면 자기사이즈 증가 후 잡아먹은 물고기 개수 초기화
    if eat_fish >= shark_size:
        shark_size += 1
        eat_fish = 0

    #  5. 잡아먹은 물고기 좌표 [nx][ny]는 초기화, queue에는 다음 좌표와 depth 0을 집어넣고 시작
    graph[px][py] = 0
    start = (px, py, 0)

print(time)
