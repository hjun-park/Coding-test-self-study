import sys

# 풀지 못함
# 참고 링크 : https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-2667%EB%B2%88-%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0-%EC%B4%88%EC%BD%94%EB%8D%94




#############################################################
#################    D F S 로 푼 예제    #####################
#############################################################
# 좌표문제는 dx, dy 만들어주기
# [좌, 상, 우, 하]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0  # 한 단지 내 집이 몇 개인지 ?
apt = []


def dfs(x, y):
    global cnt
    a[x][y] = '0'  # 현재 방문한 곳은 0으로 설정 ( 어차피 좌표값이 0인 경우는 아파트가 없는 곳이다 )
    cnt += 1  # 방문했으니 아파트 숫자 카운트

    for i in range(4):  # 현재 좌표에서 좌상우하 이동해보기
        nx = x + dx[i]
        ny = y + dy[i]

        # 바운더리를 넘어서는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        # 현재 좌표에서 좌상우하 바라봤을 때 방문하지 않은 노드가 있다면
        if a[nx][ny] == '1':
            dfs(nx, ny)


# 주의 : 방문 가능한 지점이 1 ( 아파트 있음 ) ,방문 불가능 시점 ( 아파트 없음 )
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = [list(sys.stdin.readline()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 처음부터 끝까지 탐색하는데 방문 가능한 상태(1)인 경우 단지 구성 아파트 개수 확인
            if a[i][j] == '1':
                cnt = 0
                dfs(i, j)           # DFS 순회
                apt.append(cnt)     # 순회 후에 단지 수를 저장

    print(len(apt))
    apt.sort()  # 오름차순 정렬
    for i in apt:
        print(i)


#############################################################
#################    B F S 로 푼 예제    #####################
#############################################################
# https://joosjuliet.github.io/2667/    # BFS로 푼 예제
#
# import sys
# read = lambda : sys.stdin.readline().strip()
#
# n = int(read())
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
#
# def bfs(matrix, cnt, x, y):
#     matrix[x][y]=0
#     # 이건 이제 이미 간것이다. 그래서 0으로 바꾼다
#     queue = []
#     queue.append((x, y))
#     while len(queue) > 0:
#         x, y = queue.pop()
#         for k in range(0, 4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx and nx< n and 0<= ny and ny <n:
#                 if matrix[nx][ny] == 1:
#                     cnt += 1
#                     matrix[nx][ny] = 0
#                     queue.append((nx, ny))
#     return cnt
#
# matrix = [list(map(int, list(read()))) for _ in range(n)]
# # matrix에 input값 넣기
#
# cnt = 0
# ans = []
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j]==1:
#             # 일단 1로 뭔가의 그룹이다.
#             ans.append(bfs(matrix, cnt+1, i, j))
#             # 여기서 이제 그 주위에 있는 것들 다 돌아보는것이다.
# print(len(ans))
# for i in sorted(ans):
#     print(i)