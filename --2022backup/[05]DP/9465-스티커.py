import sys

input = sys.stdin.readline

'''
    참고: https://pacific-ocean.tistory.com/197
'''

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    s = [list(map(int, input().split())) for _ in range(2)]

    # 열이 1개인 경우는 자기 자신

    # 열 3개부터 ( 이미 s에는 누적된 최댓값이 존재함 )
    # max(선택할 수 있는 바로 이전 대각선 값, 지금까지 누적되어 쌓여왔던 값)
    for i in range(1, N):
        if i == 1:
            # 열이 2개인 경우
            s[0][i] += s[1][i - 1]
            s[1][i] += s[0][i - 1]
        else:
            s[0][i] += max(s[1][i - 1], s[1][i - 2])
            s[1][i] += max(s[0][i - 1], s[0][i - 2])

    print(max(s[0][N - 1], s[1][N - 1]))
