import sys

input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
    # 1. 시간 증가
    time += 1

    # 2. 다리에서 맨 처음 요소 제거
    bridge.pop(0)

    # 3. 트럭 체크 (트럭이 다리에 다 올라갔다면 그냥 지나가는 것만 체크 )
    if bridge:
        # 4. 다리에 트럭이 올라갈 수 있는지 체크 후 트럭을 다리에서 올리거나
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.pop(0))

        #   없다면 한 칸씩 뒤로 밀림
        else:
            bridge.append(0)

print(time)
