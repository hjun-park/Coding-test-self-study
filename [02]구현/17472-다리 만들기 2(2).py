import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
number = 1  # 섬 라벨링 위한 고유번호
visited = [[False] * M for _ in range(N)]
q = deque()
edge = []  # 생성한 다리 놓는 후보 배열 (시작지, 시작지위치, 다리개수)

'''
 # 크루스칼 알고리즘 이용
 
 # 과정 [ https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-17472.-%EB%8B%A4%EB%A6%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0-2-by-Python ] 
    1) 섬마다 고유번호룰 부여 ( BFS 이용 )
    2) 섬들간 다리를 놓기 위해서 조건 파악  ( check 함수 )
    3) 크루스칼 이용하여 최소 거리 탐색 
'''

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 노드의 부모를 찾는 부분
def find(parents, v):
    if parents[v] == v:  # 부모라면
        return v
    parents[v] = find(parents, parents[v])
    return parents[v]


def union(parents, a, b):
    # a, b 각각 부모를 찾음 ( 부모끼리 이어줄 예정 )
    rootA = find(parents, a)
    rootB = find(parents, b)

    # 최소 길이를 부모로 지정
    if rootA < rootB:
        parents[rootB] = rootA  # rootB의 부모를 rootA로 지정

    else:
        parents[rootA] = rootB


def check(line):
    '''
        1. flag 설정 후 각 라인의 요소를 돈다. (start=0, cnt=0)
        2-1. 라인 요소를 돌면서 0이 아닌 값이 나오고 flag=False 라면
            flag = True 및 start를 해당 위치로 잡는다.
        2-2. 라인 요소를 돌면서 0이면서 flag가 True라면 cnt를 증가시킨다.
        2-3. 라인 요소를 돌면서 0이 아니고 flag=True이면서 start지점도 아니라면 더 확인
         2-3-1. start 값이 있으면서 cnt가 2를 넘는다면 (다리 건설 가능)
           2-3-2. edge에 해당 값이 없다면 edge에 추가한다.
         2-3-2. 다리 건설 불가능하다. (cnt를 초기화하고 start값을 해당 인덱스로 바꾼다.
        # 이것때문에 반례가 많이 잡히는건가 ?
        2-4. 해당 index가 시작지라면 cnt = 0으로 한다.

    '''
    flag = False  # 시작지가 정해지면 flag는 True (시작지 여부)
    start, cnt = 0, 0

    for i in range(len(line)):
        if line[i] != 0 and not flag:  # 시작지도 없고 바다도 아니라면
            flag = True
            start = line[i]
        elif line[i] == 0 and flag:  # 시작지가 이미 정해져 있고 바다라면
            cnt += 1
        elif line[i] != 0 and flag and start != line[i]:  # 시작지는 정해져있고 시작지 위치도 아니면서 육지인 경우
            # 다리를 놓을 수 있다면
            if cnt >= 2 and start != 0:
                if (start, line[i], cnt) not in edge:  # 다리가 등록도 안 되어 있다면
                    edge.append((start, line[i], cnt))
            # 다리를 놓을 수 없다면 초기화
            cnt = 0
            start = line[i]  # 계속 탐색하기 위해 시작지 재 지정
        elif start == line[i]:  # 시작지와 같은 섬인 경우 cnt 초기화
            cnt = 0


for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and not visited[i][j]:
            q.append((i, j))
            visited[i][j] = True

            while q:
                x, y = q.popleft()
                graph[x][y] = number  # 섬 라벨링

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 섬 영역이 있고 방문하지 않았다면 q에 넣고 라벨링 진행
                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] != 0 and not visited[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True

            # 탐색이 끝났다면 다음 라벨링을 위해 값 증가
            number += 1

# 행 탐색
for row in graph:
    if sum(row):
        check(row)

# 열 탐색 ( zip을 이용한다. )
for col in list(zip(*graph)):
    if sum(col) != 0:  # 무언가 값이 있다면
        check(col)

# 크루스칼 알고리즘을 통해 한 번에 이을 수 있는지 확인
answer = 0
edge = sorted(edge, key=lambda x: (x[2]), reverse=True)  # 다리 개수에 따라 정렬

# number가 1부터 시작하니까 간선 개수 +1 더할 필요는 없음
parents = [x for x in range(number)]  # 섬 개수만큼 생성 ( 부모의 부모는 자신값을 가지도록 )
cnt = number - 2

# 4개 섬에서는 다리는 3개만 있어도 됨 ( number 섬의 수+1, cnt = 다리 수 )
while cnt:
    try:
        start, end, count = edge.pop()

    except IndexError as e:
        print(-1)
        sys.exit(0)

    if find(parents, start) != find(parents, end):
        union(parents, start, end)
        answer += count
        cnt -= 1    # 다리를 이은 경우에만 cnt - 1

print(answer)
