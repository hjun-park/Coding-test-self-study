import sys

input = sys.stdin.readline


# dp는 거꾸로 점화식을 수립해나간다.
# 첫 번째를 떼느냐, 두 번째를 떼느냐 이 2가지이며, 점화식은 다음과 같다.
# dp[i] = max(dp[i-1], dp[i-2] + dp[i])

def solution(sticker):
    answer = 0

    dp = [0] * len(sticker)

    dp[0] = sticker[0]
    dp[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp[i] = max(dp[i-1], dp[i-2] + dp[i])

    return dp[len(sticker)-1]


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
