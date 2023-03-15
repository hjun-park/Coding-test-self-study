import sys

input = sys.stdin.readline
#
# N = int(input())
# graph = [0] * N
# result = 0

'''
    https://hellominchan.tistory.com/176
    1. N 개의 퀸을 놓아야 하기 때문에 각 행마다 1개씩 존재해야 한다. (좌우로 움직이니까)
    1-1. 행마다 한 개씩 놓는다면 가로(좌우)는 확인할 필요가 없다.
    2. 그럼 결국 세로와 대각선만을 확인하면 되는데, 세로의 경우 1차원 배열로 확인 가능
    2-1. 대각선의 경우   ↗, ↙  해당 대각선 방향 각각의 인덱스의 합들과 같다는 규칙이 있었습니다.
        (체스판에 직접 인덱스를 매겨서 더해보시면 이해가 쉽습니다. ex) (0,2) = (1,1) = (2,0) )
'''


def check(n):   # 행을 제한하는 이유는 첫번째 행부터 퀸을 놓기 시작하는데, 그 밑에는 퀸을 놓지 않은 상태
                # 굳이 퀸을 놓지 않은 행을 점검할 필요는 없다.
    for i in range(n):
        # row[n] = m의 의미
        #  n번째 행의 m번째 열 (n, m)
        # row[n] == row[i]는 서로 다른 행에 같은 열로 놓인 경우
        # or
        # 대각선의 경우
        # 열은 열끼리 빼고 행은 행끼리 뺐을 때 서로 같은 값이 되어야 같은 대각선상에 놓였다고 할 수 있다.
        # (0,2) == (1,1) == (2,0) , (0,2) == (2,0)
        if row[n] == row[i] or abs(row[n] - row[i]) == n - i:
            return 0
    return 1


def dfs(n):
    global res
    if n == N:
        res += 1
    else:
        for i in range(N):
            row[n] = i  # n번째 행의 i번째 열에 퀸이 있다고 가정
            if check(n):
                dfs(n + 1)


N = int(input())
row = [0] * N
res = 0
dfs(0)
print(res)
