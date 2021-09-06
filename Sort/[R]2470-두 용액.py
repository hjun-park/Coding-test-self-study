import sys

# 조합하여 0에 가까운 수를 만들어야 함

input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))
# solution = list(map(int, input().split(' ')))
# print(s)
# print(solution)
s.sort()

# 이중 포인터 설정
left = 0
right = N-1

min_value = 2e+9+1

answer = []

# 이중포인터 진행
while left < right:
    s_left = s[left]
    s_right = s[right]

    total = s_left + s_right

    # 두 용액 합이 0과 가까운 용액을 정답에 달아주기
    if abs(total) < min_value:
        min_value = abs(total)
        answer = [s_left, s_right]

    # 두 용액 합이 0보다 작다면 왼쪽값을, 0보다 크다면 오른쪽을 줄이기
    if total < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])


