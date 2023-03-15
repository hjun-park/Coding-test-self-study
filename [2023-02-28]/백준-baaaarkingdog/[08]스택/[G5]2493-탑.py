import sys

input = sys.stdin.readline

n = int(input().rstrip())
tower_list = list(map(int, input().split()))
result = [0] * n  # idx에서 레이저를 쐈을 때 몇 번째 탑에서 수신하는지 담을 결과 배열
stack = []  # 탑의 idx가 담김

# 1) 문제에서는 끝에서 레이저를 쏴서 수신하지만,
# 여기서는 정방향으로 루프를 돌아 거꾸로 확인
for i in range(n):
    tower = tower_list[i]  # 기준이 되는 tower를 잡음

    # stack이 비어있지 않으며
    # 기준 타워(tower)보다 직전의 tower(tower_list[stack[-1]])가 작다면
    # 레이저를 받지 못함
    while stack and tower_list[stack[-1]] < tower:
        stack.pop()

    # 제거해도 아직도 남아 있다면 레이저를 받을 수 있는 탑이다.
    if stack:
        result[i] = stack[-1] + 1

    stack.append(i)

print(' '.join(map(str, result)))
