import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(N)]


# 구현 참고: https://enhjh.tistory.com/43
# 1) 위아래, 왼쪽오른쪽 개수를 세는 방법
# 2) 서로 자리를 바꾸는 경우
# 교환 -> 체크 -> 복구

def check():
    check_count = 1
    for i in range(N):
        # 열 순회하며 연속된 숫자 세기
        cnt = 1
        for j in range(1, N):
            if graph[i][j] == graph[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            check_count = max(check_count, cnt)

        # 행 순회하면서 연속된 숫자 세기
        cnt = 1
        for j in range(1, N):
            if graph[j][i] == graph[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            check_count = max(check_count, cnt)

    return check_count


answer = 0
for i in range(N):
    for j in range(N):
        # 열 바꾸기
        if j + 1 < N:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

            temp = check()
            answer = max(answer, temp)

            # 복구
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

        # 행 바꾸기
        if i + 1 < N:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]

            temp = check()
            answer = max(answer, temp)

            # 복구
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]

print(answer)
