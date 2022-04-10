import sys

input = sys.stdin.readline

graph = [list(input().rstrip()) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]

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

temp = []
cnt = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def dfs(x, y):
    global cnt, visited

    # visited[x][y] = True

    if len(temp) == 7:
        if temp.count('S') >= 4:
            print(*temp)

            for row in visited:
                print(*row)
            cnt += 1
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visited[nx][ny]:
                temp.append(graph[nx][ny])
                visited[nx][ny] = True
                dfs(nx, ny)
                visited[nx][ny] = False
                temp.pop()


# 로직 타기
for i in range(5):
    for j in range(5):
        visited[i][j] = True
        temp.append(graph[i][j])
        dfs(i, j)
        temp.pop()
        visited[i][j] = False

print(cnt)
