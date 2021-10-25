import sys

input = sys.stdin.readline


def binary_search(target, start, end):
    answer = 0
    while start <= end:
        # 1) 항상 start = 1, end = max값
        mid = (start + end) // 2
        # 2) 중앙값을 더한 값이 Z보다 작다면 start 위치를 mid + 1로 옮김
        if ((Y + mid) * 100) // (X + mid) <= target:
            start = mid + 1
        # 3) 크다면 일단 정답이니까 answer에 mid값을 담고 right 위치 조정
        else:
            answer = mid
            end = mid - 1
    # 4) while끝에 answer 출력
    print(answer)


X, Y = map(int, input().split())
Z = (Y * 100) // X
if Z >= 99:
    print(-1)
else:
    binary_search(Z, 1, X)




# =============================
# 시간초과
# =============================
# X, Y = map(int, input().split())
# if X == Y:
#     print(-1)
#     sys.exit(0)
# Z = int(Y / X * 100)  //  이렇게 계산하면 부동소수점 오차 남
#
# start = 1
# end = X
#
# Z_bk = Z
# count = 0
# while True:
#     X += 1
#     Y += 1
#     count += 1
#     if int(Y / X * 100) > Z:
#         print(count)
#         break
#     else:
#         continue


# binary_search(Z + 1, start, end)
