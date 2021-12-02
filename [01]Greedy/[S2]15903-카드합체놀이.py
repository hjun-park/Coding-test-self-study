import sys


# 1. 입력
n, m = map(int, input().split())
cards = list(map(int, sys.stdin.readline().split()))

# 2. 루프돌면서 처음엔 sorting,
for _ in range(m):
    cards.sort()

    # 3. a[0] a[1] 추출해서 더한 후에 a[0], a[1] 대입
    merged_value = cards[0] + cards[1]
    cards[0] = merged_value
    cards[1] = merged_value

# 루프 반복하고

# 마지막에는 전체 합을 출력
print(sum(cards))
