import sys

input = sys.stdin.readline


# dp는 거꾸로 점화식을 수립해나간다.
# 첫 번째를 떼느냐, 두 번째를 떼느냐 이 2가지이며, 점화식은 다음과 같다.
# dp[i] = max(dp[i-1], dp[i-2] + dp[i])

def solution(sticker):
    # table[i] = i번째 스티커를 떼는 경우 최댓값
    # 맨 앞 스티커를 떼는지 아닌지 -> 맨 뒤 스티커에 영향을 준다

    if len(sticker) == 1:
        return sticker[0]

    # 1. 맨 앞 스티커를 떼는 경우
    dp = [0 for _ in range(len(sticker))]
    dp[0], dp[1] = sticker[0], sticker[0]

    for i in range(2, len(sticker) - 1):    # 이 부분에서 차이
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    front_max = max(dp)

    # 2. 맨 앞 스티커를 떼지 않는 경우
    dp = [0 for _ in range(len(sticker))]
    dp[0], dp[1] = 0, sticker[1]

    for i in range(2, len(sticker)):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])

    back_max = max(dp)

    return max(front_max, back_max)


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
