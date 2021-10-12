import sys

input = sys.stdin.readline

N, M = map(int, input().split())

min_p, min_o = 1001, 1001
for _ in range(M):
    package, one = map(int, input().split())

    min_p = min(min_p, package)
    min_o = min(min_o, one)

div = N // 6
rest = N % 6


# 패키지가 저렴한 경우 패키지로 사고
if min_p < min_o * 6:
    # 남는 건 패키지로 구매하는 것이 저렴한 경우
    if min_p < rest * min_o:
        print(div * min_p + min_p)
    # 남는거 그냥 낱개로 구매하는 것이 저렴한 경우
    else:
        print(div * min_p + rest * min_o)

# 낱개가 저렴한 경우
elif min_p >= min_o * 6:
    print(min_o * N)
