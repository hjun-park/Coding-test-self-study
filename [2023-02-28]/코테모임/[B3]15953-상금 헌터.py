import sys

input = sys.stdin.readline

T = int(input().rstrip())
money2017 = 0
money2018 = 0

kakao2017 = [(500, 1), (300, 3), (200, 6), (50, 10), (30, 15), (10, 21)]
kakao2018 = [(512, 1), (256, 3), (128, 7), (64, 15), (32, 31)]


def get_money(kakao, rank):
    for m, p in kakao:
        if p >= rank:  # 자신의 순위 값보다 더 커지는 순간 그 순위 금액을 가져감
            return m
    return 0


for _ in range(T):
    a, b = map(int, input().split())
    total = 0

    # a와 b가 0이 아닌 경우에만 수행
    if a != 0:
        total += get_money(kakao2017, a)
    if b != 0:
        total += get_money(kakao2018, b)

    print(total * 10_000)


