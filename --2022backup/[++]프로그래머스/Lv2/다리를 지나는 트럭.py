def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    cnt = 0
    while len(bridge):
        cnt += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return cnt


print(solution(2, 10, [7, 4, 5, 6]))
