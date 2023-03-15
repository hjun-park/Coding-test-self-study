import sys

n, m = map(int, input().split())
graph = []

# 요구하는 좌표 입력 받음
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 좌표 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 최댓값 좌표 설정
result = 0
max_val = max(map(max, graph))

# history 배열
history = [[False] * m for _ in range(n)]

def DFS(depth, x, y, graph_score):
    global result
    # depth 연산에 따라서 달라짐

    # 1) 처음 depth를 지정하고 들어왔기 때문에 3번 더 들어갈 수 있음
    # 만약에 result 값보다 현재 graph_score + ( 남은 depth * max ) 값이 더 작다면 더 볼 것도 없음
    if graph_score + (3-depth) * max_val <= result:
        return
    # 만약 depth가 3이라면 (마지막) DFS를 하지 않고 현재 값(graph_score)과 최댓값 result를 비교하여 갱신
    if depth == 3:
        result = max(result, graph_score)
    else:   # DFS
        # 4방향 돌면서 체크
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]


            if nx < 0  or ny < 0 or nx >= n or ny >= m or history[nx][ny]:
                continue

            # 'ㅜ' 의 가운데 점에서는 실제로 이동하지 않고 더하기만 하고 계산
            if depth == 1:
                # DFS 돌기 전 방문기록 남기기
                history[nx][ny] = True
                DFS(depth + 1, x, y, graph_score + graph[nx][ny])
                history[nx][ny] = False
            history[nx][ny] = True
            DFS(depth + 1, nx, ny, graph_score + graph[nx][ny])
            history[nx][ny] = False


# 각 요소 순회하며 DFS 탐색
for i in range(n):
    for j in range(m):
        history[i][j] = True
        DFS(0, i, j, graph[i][j])
        history[i][j] = False

print(result)

