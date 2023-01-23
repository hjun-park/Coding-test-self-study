import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())
_min = int(1e9)
_max = -int(1e9)


# func(연산자, )
def logic(depth, num, plus, minus, mul, div):
    global _min, _max
    # base condition
    if depth == N - 1:
        _min = min(_min, num)
        _max = max(_max, num)
        return

    # TODO: 다시 고친 부분
    # TODO : 주의점 A // B를 할 때 제수가 마이너스라면 무조건 0이 나옴
    # TODO : 따라서 0이 나오지 않게 하려면 int(A / B)를 사용해야 함
    if plus > 0:
        logic(depth + 1, num + A[depth + 1], plus - 1, minus, mul, div)
    if minus > 0:
        logic(depth + 1, num - A[depth + 1], plus, minus - 1, mul, div)
    if mul > 0:
        logic(depth + 1, num * A[depth + 1], plus, minus, mul - 1, div)
    if div > 0:
        logic(depth + 1, int(num / A[depth + 1]), plus, minus, mul, div - 1)

    # TODO: 내가 했던 부분 ( for문 돌릴 필요 없음 )
    # for a in A[1:]:
    #     if plus > 0:
    #         rst += a
    #         logic(depth + 1, plus - 1, minus, mul, div)
    #         rst -= a
    #
    #     elif minus > 0:
    #         rst -= a
    #         logic(depth + 1, plus, minus - 1, mul, div)
    #         rst += a
    #     elif mul > 0:
    #         logic(depth + 1, plus, minus, mul - 1, div)
    #     elif div > 0:
    #         logic(depth + 1, plus, minus, mul, div - 1)


logic(0, A[0], plus, minus, mul, div)
print(_max)
print(_min)
