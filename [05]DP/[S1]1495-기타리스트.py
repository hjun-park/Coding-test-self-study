import sys

input = sys.stdin.readline

# M은 그 이상 갈 수 없는 최대 볼륨
n, s, m = map(int, input().split())
vol = list(map(int, input().split()))

# 1) 최대 볼륨까지의 DP 2개를 선언 ( 2차원 배열을 사용해도 됨 )
dp1 = [False] * (m + 1)
dp2 = [False] * (m + 1)

# 2-0) 처음 시작 볼륨에 대해 존재 처리 (dp1)
dp1[s] = True

# 2) 볼륨리스트 순회
for v in vol:
    # 2-1) 최대 볼륨까지 순회
    for i in range(m + 1):
        # 2-2) dp1에 값이 있으면서 i-v, i+v 조건에 만족하면 dp2에 대해 True 갱신
        if dp1[i]:
            if i + v <= m:
                dp2[i + v] = True
            if i - v >= 0:
                dp2[i - v] = True
    # 2-3) 2-1 for문 끝나면 dp1에 dp2 대입
    dp1 = dp2
    dp2 = [False] * (m + 1)
# 따로 진행하는 이유는 dp1은 매번 갱신된 볼륨에 대해 순환해주기 위함이고
# dp2는 i + v,  i - v 작업용이다.


# 3) 최댓값부터 먼저 순환하면서 dp1의 인덱스 값 존재 확인, 없으면 -1
ans = -1
for i in range(m, -1, -1):
    if dp1[i]:
        ans = i
        break

print(ans)

# dp1[s] = 1
# for v in vol:
#     for i in range(m + 1):
#         if dp1[i]:
#             if i + v <= m:
#                 dp2[i + v] = 1
#             if i - v >= 0:
#                 dp2[i - v] = 1
#     dp1 = dp2
#     dp2 = [0] * (m + 1)

# ans = -1
# for i in range(m, -1, -1):
#     if dp1[i]:
#         ans = i
#         break
# print(ans)
#
