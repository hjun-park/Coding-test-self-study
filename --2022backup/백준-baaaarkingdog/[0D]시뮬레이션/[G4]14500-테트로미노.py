import sys

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

'''
 1. 회전이나 대칭 가능 ( 4칸 가는데면 모든 곳 다 이동 가능 )
 2. 칸에 있는 수들의 합을 최대로
 3. 테트로미노 하나를 놓아서 합을 최대로

-> 모든 방향에 대해서 rotation 가능
'''

# 2. 모든 테트로미노에 놓을 수 있는지 확인 ( +대칭 )
# Def Func : (depth, x, y, _sum)
'''
    ㅁ ㅁ ㅁ ㅁ
    ㅁ ㅁ ㅁ 
    ㅁ ㅁ
    ㅁ
'''

_max = -1


def dfs(depth, x, y, _sum):
    global _max
    # Base condition
    if depth == 3:
        _max = max(_max, _sum)
        return

    # Recursion Logic
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:

                # 'ㅏ', 'ㅜ' 이런 애들
                # 제자리걸음만 하고 다음 값은 그냥 더함
                # 다시 돌아오기 때문에 직접 갈 필요는 없음
                if depth == 1:
                    visited[nx][ny] = True
                    dfs(depth + 1, x, y, _sum + graph[nx][ny])
                    visited[nx][ny] = False

                # 나머지 모든 모양들
                visited[nx][ny] = True
                dfs(depth + 1, nx, ny, _sum + graph[nx][ny])
                visited[nx][ny] = False


# 1. 리스트 처음부터 끝까지 순회
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(0, i, j, graph[i][j])
        visited[i][j] = False


print(_max)