import sys
from collections import deque

# n: NxN
# l, r: 두 인구 차가 l보다 크고 r보다 작으면 연합
n, l, r = map(int, input().split())

# N x N 정보 전체 입력 받음
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 좌상우하 ( 4사분면 생각 )
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0


# 특정 위치에서 출발하여 모든 연합을 체크 및 갱신
def process(x, y, index):       # 여기서 union은 전역변수
    # (x, y) 위치와 연결된 나라(정보)를 담는 리스트
    united = []
    united.append((x, y))

    # 너비 우선 탐색(BFS)를 이용한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index  # 현재 연합의 번호 할당
    summary = graph[x][y]  # 현재 연합의 전체 인구 수
    count = 1  # 현재 연합의 국가 수

    '''
        union: 해당 x, y좌표의 연합국이 속하는 번호 (index)
        united: process 함수 실행 당시에만 볼 수 있는 서로 속한 연합국, 좌표를 리스트로 구성되어 있음
    '''

    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4방향 탐색    // 주변 연합국 탐색 //
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 바로 옆에 있는 나라를 확인하며
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:  # 정상적인 위치 + 조사하지 않았을 때
                # 옆에 있는 나라와 인구 차이가 L명 이상 R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))  # BFS 위해서 ( 연합에 추가된 국가도 BFS로 퍼뜨리기 위해서 추가 )

                    # 연합에 추가
                    union[nx][ny] = index   # index는 연합 번호
                    summary += graph[nx][ny]    # 동일한 연합은 인구 수 누적 계산
                    count += 1                  # 연합 인구이동 위해 구하는 연합국 개수 count
                    united.append((nx, ny))     # 새로운 연합국 좌표 추가
    # 연합 국가끼리 인구 분배
    for i, j in united:             # 연합에 속한 국가만큼 count 개수로 나눔
        graph[i][j] = summary // count
    return


total_count = 0

# 더 이상 인구 이동할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            print(f'union: {i}, {j}')
            if union[i][j] == -1:  # 해당 나라가 아직 처리되지 않았다면 처리
                print('union process')
                process(i, j, index)    # index: 연합 번호
                index += 1

    # 모든 인구 이동이 끝난 이후
    # 아래 print를 거치는 경우:
    print('check_val', index)
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)
