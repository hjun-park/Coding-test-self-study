import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

dic = {0: 0, 1: 0}

# 1) 함수 정의
# def logic(n, r, c)

# 2) base condition
# n이 1이라면 1x1 사이즈이므로 해당 색의 색종이를 더한다.

# 3) 재귀식
# 전체 돌면서 다른게 하나라도 발견된다면 2로 나누어 쪼개면 된다.
'''
    half = 1<<(n-1)
    logic(n//2, r, c)
    logic(n//2, r, c + half)
    logic(n//2, r + half, c)
    logic(n//2, r + half, c + half)
    return
'''


def logic(n, r, c):
    if n == 1:
        dic[graph[r][c]] += 1
        return

    # 재귀식
    half = n // 2
    for i in range(r, r + n):
        for j in range(c, c + n):
            if graph[r][c] != graph[i][j]:
                logic(n // 2, r, c)
                logic(n // 2, r, c + half)
                logic(n // 2, r + half, c)
                logic(n // 2, r + half, c + half)
                return

    # 해당 코드를 돈단 얘기는 모든 값이 동일해서 하나의 사각형으로 생성 가능하단 의미
    dic[graph[r][c]] += 1
    return


logic(N, 0, 0)
print(dic[0])
print(dic[1])
