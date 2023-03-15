import sys

# 첫 번째, 끝 자리가 1이면 리스트로 변환하여 1을 빼준다.
# 두 번째, 2로 나눈다.

a, b = map(int, input().split())

count = 1
while True:
    if a == b:  # 같으면 break
        break
    elif a > b or (b % 10 != 1 and b % 2 != 0):   # 10으로 나눈 나머지가 1이 아니거나 2로 나누어지지 않는 경우
        count = -1
        break
    elif b % 10 == 1:   # 끝자리가 1로 끝나는 경우
        b //= 10
        count += 1
    elif b % 2 == 0:    # 2로 나누어지는 경우
        b //= 2
        count += 1

print(count)


