import sys

input = sys.stdin.readline

'''
    핵심: 어렸을 때 공부했던 서로 만나는 지점은 더해주는 방법 + DP 이용
    참고: https://suri78.tistory.com/207
    
    1. 해당 좌표까지 얼마나 갈 수 있는지에 대한 DP 좌표 생성
    2. 행이 1개인 경우 가는 모든 방법은 1가지 ( dp[0] = [1] * m )
    3. k가 0인 경우
    3-1. 행이 1부터 시작, n까지, 열은 m까지 해서 끝점까지 이동할 수 있는 모든 경우의 수를 구한다. 
      - 1부터 시작하는 이유는 행이 1이라면 어차피 길은 1가지 밖에 없다. 
      - 열이 0이라면 1을 지정하고, 아니라면 점화식 계산 dp[i-1][j] + dp[i][j-1]
      
    4. k가 있는 경우
      4-1. k-1행과 열 m을 집어넣어서 divmod를 통해 x,y를 구한다.
      4-2. k 위쪽의 사각형 경로 개수를 구한다. 
        - 1부터 x, y 까지만 순회하고, 이동하는 경우를 3-1처럼 구한다.
        - 순회를 다 하면 x, y 좌표가 처음부터 K까지의 경로이다. 
      4-3. k 아래쪽 사각형 경로 개수를 구한다.
        - x+1, y+1부터 n, m전까지 순회하고 
        - 순회를 다 하게되면 마지막좌표 (dp[-1][-1])가 나오게 된다.
      4-4. (4-2, 4-3 결과를 서로 곱해주면 최종 경로 개수가 나온다)
'''

# 행, 열, O
N, M, K = map(int, input().split())

dp = [[0] * M for _ in range(N)]
# 2.행이 1개인 경우 가는 모든 방법은 1가지
dp[0] = [1] * M

if K == 0:
    for i in range(1, N):
        for j in range(M):
            # 열이 1개라면 가는 경로는 1개
            # 아니라면 점화식 d[i-1][j] + d[i][j-1]
            dp[i][j] = 1 if j == 0 else dp[i - 1][j] + dp[i][j - 1]
    print(dp[-1][-1])  # 해당 경로까지 가는 길을 출력

else:
    # 몫은 x, 나머지는 y에 들어감
    x, y = divmod(K - 1, M)  # K의 x, y 좌표를 구함

    # 처음부터 K까지의 경로를 구함
    for i in range(1, x + 1):
        for j in range(y + 1):
            dp[i][j] = 1 if j == 0 else dp[i - 1][j] + dp[i][j - 1]
    first = dp[x][y]

    # K부터 마지막 좌표까지의 경로를 구함
    dp[x] = [1] * M  # K아래의 첫 행은 무조건 1
    for i in range(x + 1, N):  # 행은 항상 +1 상태에서 시작함
        for j in range(y, M):  # j == y는 j==0와 똑같음(첫 행을 의미함)
            dp[i][j] = 1 if j == y else dp[i - 1][j] + dp[i][j - 1]
    second = dp[-1][-1]

    print(first * second)
