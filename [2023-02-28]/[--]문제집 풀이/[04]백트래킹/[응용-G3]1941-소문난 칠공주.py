import sys

input = sys.stdin.readline

# graph = [list(input().rstrip()) for _ in range(5)]
# visited = [[False] * 5 for _ in range(5)]

'''
    [참고]
    https://velog.io/@moonseok/%EB%B0%B1%EC%A4%801941-%EC%86%8C%EB%AC%B8%EB%82%9C-%EC%B9%A0%EA%B3%B5%EC%A3%BC
    https://codinghani.tistory.com/59 -> 접근방법 잘 설명되어 있음
'''

'''
 - 이다솜파(S) vs 임도연파(Y)
    [소문난 칠공주]
    1) 7명의 여학생 구성
    2) 7명자리 반드시 가로세로 
    3) 굳이 이다솜파(S)로만 구성할 필요는 없다
    4) 7명 중 적어도 이다솜파(S)는 4명 이상
    
    [로직]
    1)  
    
    [구할 것]
    1) 모든 경우의 수
    
    [base condition]
    if len(temp) == 7:
        temp.count(S) >= 4:
            print(S)
            return
        return
        
    [define]
    def logic(x, y):
    
    [recursion logic]
    
'''
arr = [input() for x in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * 5 for _ in range(5)]
result = 0
temp = []


def check(s):
    global visited
    x = s // 5
    y = s % 5

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visited[nx][ny]:
                if (nx * 5 + ny) in temp:
                    visited[nx][ny] = True
                    check((nx * 5 + ny))


def dfs(cnt, idx, yn):
    global result
    global visited

    # 임도연파를 4번 넘게 뽑았거나 남은 인덱스를 다 뽑는다 해도 7번을 만족 못할 것 같은 경우
    if yn >= 4 or 25 - idx < 7 - cnt:
        return

    if cnt == 7:
        check(temp[0])  # DFS로 순환할 수 있는지 체크
        if sum(sum(visited, [])) == 7:  # 행렬 (2차원 배열) 총합 구하기 (방문한게 정확히 7개라면)
            result += 1  # 조건에 맞으므로 결괏값 증가
        visited = [[0 for _ in range(5)] for _ in range(5)] # 방문 초기화
        return

    x = idx // 5  # 1차원배열에서의 5는 (1, 0)으로 표현될 수 있다.
    y = idx % 5

    # for i in range(25):
    temp.append(idx)
    if arr[x][y] == 'Y':
        dfs(cnt + 1, idx + 1, yn + 1)  # Y인 경우 DFS
    else:
        dfs(cnt + 1, idx + 1, yn)  # S인 경우 DFS
    temp.pop()

    dfs(cnt, idx + 1, yn)  # 복구 후 다음 영역에서 다시 DFS 시작


dfs(0, 0, 0)
print(result)

# 시간초과 코드
# temp = []
# cnt = 0
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
#
#
# def dfs(x, y):
#     global cnt, visited
#
#     # visited[x][y] = True
#     if temp.count('Y') >= 4 or
#
#     if len(temp) == 7:
#         if temp.count('S') >= 4:
#             print(*temp)
#
#             for row in visited:
#                 print(*row)
#             cnt += 1
#         return
#
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#
#         if 0 <= nx < 5 and 0 <= ny < 5:
#             if not visited[nx][ny]:
#                 temp.append(graph[nx][ny])
#                 visited[nx][ny] = True
#                 dfs(nx, ny)
#                 visited[nx][ny] = False
#                 temp.pop()
#
#
# # 로직 타기
# for i in range(5):
#     for j in range(5):
#         visited[i][j] = True
#         temp.append(graph[i][j])
#         dfs(i, j)
#         temp.pop()
#         visited[i][j] = False
#
# print(cnt)
