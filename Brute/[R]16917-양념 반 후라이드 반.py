import sys

input = sys.stdin.readline

# 양가, 후가, 반가, 양념최소, 후라이드최소
A, B, C, X, Y = map(int, input().split())

# 반반이 비싼 경우
if A + B < C * 2:
    print(A * X + B * Y)
else:
    price = min(X, Y) * 2 * C  # 양념, 후라이드 중 적은 치킨을 반반으로 교체
    if X >= Y:
        less_chicken = X - Y
        price += min(A * less_chicken, 2 * C * less_chicken)  # 치킨이 남더라도 반반을 더 시키는 경우도 있음
    else:
        less_chicken = Y - X
        price += min(B * less_chicken, 2 * C * less_chicken)
    print(price)
