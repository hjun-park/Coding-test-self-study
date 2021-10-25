import sys

'''
    2021-07-01
    [시작 체크 리스트]
    V       15분 지났으나 발상 불가 또는 아예 다른 길
            20-30분 보다 더 걸려서 코드 완성
            코드는 다 돌아가는데 효율성에서 걸림
            코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
            중간 정도 이해함
    V       완벽히 이해함

    [첨언]
     - 규칙을 찾으면 쉽게 풀었을 문제

'''

'''
    [접근]
        # 점화식: d[i] = min(dp[i-j]) + 1
        # 예를 들어 i가 16이라고 했을때 i보다 작거나 같은 제곱수는 1, 4, 9, 16이다.
        # dp[i - 1], dp[i - 4], dp[i - 9], dp[i - 16]중
        # 가장 작은 값은 0이고 여기에 1을 더한 값을 dp[i]에 넣어준다.
'''

n = int(input())
d = [0] * (n+1)

for i in range(1, n+1):
    d[i] = i
    for j in range(1, i):
        # 제곱한 값이 찾는 값보다 더 크다면 다음 숫자로 탐색
        if (j * j) > i:
            break

        # 만약 기존에 있는 값보다 새로 구한 값이 더 작다면
        # 값을 새로 갱신한다.
        if d[i] > d[i - (j*j)] + 1:
            d[i] = d[i - (j*j)] + 1

print(d[n])



# sq = [x * x for x in range(1, 317)]
#
# for i in range(1, n+1):
#     s = []
#     for j in sq:
#         if j > i:
#             break
#         s.append(d[i-j])
#     d[i] = min(s) + 1
# print(d[n])
#
