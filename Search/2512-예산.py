import sys

input = sys.stdin.readline


def binary_search(target, start, end):
    while start <= end:
        total = 0
        mid = (start + end) // 2

        # 1) 요청예산을 돌면서 total값 연산 (mid보다 크면 mid로 예산 산정)
        for budget in req_budget:
            if budget > mid:
                total += mid
            else:
                total += budget

        # 2) total값이 target보다 크다면 mid값을 줄인다.
        if total <= target:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


N = int(input())  # 지방 수
req_budget = list(map(int, input().split()))  # 지방의 예산 요청
M = int(input())  # 총 예산

req_budget.sort()
# 1) 모든 요청 배정될 수 있는 경우라면 그대로 배정한다.
if sum(req_budget) <= M:
    print(max(req_budget))
    sys.exit(0)

# 2) 모든 요청이 배정될 수 없다면 상한선을 정한다 ( 넘어가면 상한선, 낮으면 그냥 그대로 배정 )
start = 1
end = max(req_budget)

binary_search(M, start, end)
