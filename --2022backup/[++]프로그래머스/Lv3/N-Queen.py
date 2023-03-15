import sys

input = sys.stdin.readline

answer = 0
last_row = 0  # 마지막 행
row = []


def check(n):
    for i in range(n):

        if row[n] == row[i]:  # 다른 행이지만 같은 값(열)에 퀸이 존재한다면 세로(열)상 같은 위치
            return False

        if abs(row[n] - row[i]) == n - i:  # 열끼리 뺀 것과 행끼리 뺐을 때 같으면 대각선상 같은 위치
            return False

    return True


def dfs(n):
    global answer, last_row

    # n은 행인데 0번째 행부터 시작
    if n == last_row:  # 마지막 행까지 왔다면 방법을 찾은 것
        answer += 1
    else:  # 아니라면
        for i in range(last_row):  # 각 열을 탐색
            row[n] = i  # n번째 행 i열에 퀸을 놓음
            if check(n):  # n번째 행 i열에 퀸을 놓았을 때 겹치는지 탐색
                dfs(n + 1)  # 퀸을 놓을 수 있다면 다음 행에 놓을 퀸 위치를 탐색


def solution(n):
    global row, last_row
    row = [0] * n
    last_row = n
    dfs(0)

    return answer


print(solution(4))
