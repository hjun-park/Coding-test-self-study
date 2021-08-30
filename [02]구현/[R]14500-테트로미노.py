import sys

'''
 https://www.landlordgang.xyz/49
 1) 요구하는 입력 받음 + 좌표 설정 ( 좌 상 우 하 )
 2) 좌표 설정 ( 좌 상 우 하 ) + DFS 각 위치 기록할 history 배열 선언 
 3) 각 요소를 순환하면서 DFS를 돌 때에는 history를 True로 설정하고 진입
 4) DFS 함수 내부
 4-1) 이동좌표 dx, dy 연산, 범위 확인
 4-2) 범위 확인에 따른 로직 설계
'''


# 종이 가로x세로
n, m = map(int, input().split())
graph = []

# 입력
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 좌표 설정 ( 좌 상 우 하 )
nx = [-1, 0, 1, 0]
ny = [0, 1, 0, -1]


def DFS(depth, x, y, graph_score):
    global result

    # depth 좌표가 있으면 depth가 4->3 된다는데 그 이유는 ?
    # => graph_score는 1x1 정사각형 1개사이즈, + 나머지 3칸 해서 depth가 3개만 있어도 됨
    # 그래프 점수 + (남은깊이 * 최댓값)이 현재까지의 최댓값보다 작다면
    # 볼 필요도 없이 리턴

    # 1) 처음 depth를 지정하고 들어왔기 때문에 3번 더 들어갈 수 있음
    # 만약에 result 값보다 현재 graph_score + ( 남은 depth * max ) 값이 더 작다면 더 볼 것도 없음
    if graph_score + (3 - depth) * max_val <= result:
        return
    # 만약 depth가 3이라면 (마지막) DFS를 하지 않고 현재 값(graph_score)과 최댓값 result를 비교하여 갱
    if depth == 3:
        result = max(result, graph_score)
        return
    else:
        # 4방향을 돌면서 순회
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            # 이동할 좌표가 범위를 벗어나거나 이미 방문한 좌표라면 패스
            if dx < 0 or dx >= n or dy < 0 or dy >= m or history[dx][dy]:
                continue

            # depth=1은  'ㅜ' 인 경우만 필요함, dx, dy가 아닌 x, y를 넘김
            # 이유는 두 번째 가운데 위치에서는 끝 점수만 바라볼거라서,
            # 이동하지않고 점수만 더하는 방식
            # ( 이동하면 다시 복귀해야 하므로 )
            if depth == 1:
                history[dx][dy] = True
                DFS(depth + 1, x, y, graph_score + graph[dx][dy])
                history[dx][dy] = False
            history[dx][dy] = True
            DFS(depth + 1, dx, dy, graph_score + graph[dx][dy])
            history[dx][dy] = False


# 1) 결과 선언 및 행렬에서 최댓값 찾음
result = 0
max_val = max(map(max, graph))

# 히스토리 관련 설정
history = [[False] * m for _ in range(n)]

# 각 요소를 순환하면서 도형이 만들어지는 경우를 파악, 대입
for i in range(n):
    for j in range(m):
        history[i][j] = True  # 방문한 경우 ?
        DFS(0, i, j, graph[i][j])  # depth, 해당좌표, 점수
        history[i][j] = False
print(result)
