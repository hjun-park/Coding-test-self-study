import sys

input = sys.stdin.readline


def binary_search_before(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        account = M * mid

        for price in consume:
            # 0) K원 인출
            account -= mid

            # 1) 모자라는지 확인
            if mid - price < 0:
                # 1-1) 모자라면 남은 금액을 통장에 집어넣고 다시 K원 인출
                account += (mid - price)
                account -= mid

            # 1-2) 모자르지 않다면 남은금액을 집어넣는다.
            else:
                account += (mid - price)

        # 남은 금액 확인
        if account < 0:  # 부족하다면 mid를 확장
            start = mid + 1
            print(start)
        else:  # 남는다면
            result = end
            end = mid - 1
            print(end)

    print(result)


def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        charge = mid    # 잔액
        count = 1       # 충전 횟수 ( 한 번 충전하고 시작 )

        for i in range(N):
            if charge < consume[i]: # 소비해야할 금액이 충전금액보다 더 많다면
                charge = mid        # 충전을 더 한다.
                count += 1
            charge -= consume[i]    # 충전금액만큼 차감한다.

        # 충전횟수가 많다면 금액이 부족한 것
        if count > M or mid < max(consume):
            start = mid + 1
        else:
            end = mid - 1
            result = mid

    print(result)


N, M = map(int, input().split())
consume = []

for _ in range(N):
    consume.append(int(input()))

start = min(consume)
end = sum(consume)
binary_search(start, end)
