import sys

input = sys.stdin.readline

# 1) 함수의 정의
# def logic(사이즈(n), 행 범위(r), 열 범위(c)):

# 2) base condition
# if n == 1: print(graph[r][c] + ')')

# 3) 재귀식
# n이 줄어든 최초의 경우에만 '('을 추가
# for문 돌면서 같지 않으면 logic 재귀를 타고,
# 만약 다 같아서 for문을 탈출했다면 print(graph[r][c] + ')')


N = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
code = []

# 1) 함수 정의
def logic(n, r, c):
    # 2) base condition
    if n == 1:
        code.append(graph[r][c])
        return

    # 3) 재귀식
    half = n // 2
    for i in range(r, r + n):
        for j in range(c, c + n):
            if graph[i][j] != graph[r][c]:
                # 나누는 순간 괄호 열기
                code.append('(')

                logic(n // 2, r, c)
                logic(n // 2, r, c + half)
                logic(n // 2, r + half, c)
                logic(n // 2, r + half, c + half)

                # 한 구간이 끝나면 닫는 괄호
                code.append(')')
                return

    code.append(graph[r][c])
    return


logic(N, 0, 0)
print(''.join(map(str, code)))
