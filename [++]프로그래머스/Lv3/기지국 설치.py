import sys, math

input = sys.stdin.readline


def solution(n, stations, w):

    # 0. [초기화] 기지국 사이의 거리를 가지고 구현한다.
    distance = []
    count = 0

    '''
        1. 기지국 간의 전파가 닿지 않는 거리
        2. 첫 번째 기지국과 첫 번째 아파트와 닿지 않는 거리
        3. 마지막 기지국과 마지막 아파트와 닿지 않는 거리
        
        를 리스트에 집어넣고 연산을 한다.
    '''

    # 1. 두 기지국 사이 통신이 안 되는 구간 구하기 위해선 기지국 2개부터 필요,
    # 따라서 1부터 시작
    for i in range(1, len(stations)):
        distance.append((stations[i] - w - 1) - (stations[i-1] + w))

    # 2. 첫 번째 기지국 전파와 첫 번째 아파트와 닿지 않는 거리
    #    0 또는 음수가 나오면 닿지 않는 거리는 없다.
    #    -1한 이유는 해당 자리가 아파트가 있다면 전파가 닿지않는다는 의미
    distance.append(stations[0]-w-1)

    # 3. 마지막 기지국 전파와 마지막 아파트와 닿지 않는거리
    #    전체 아파트 개수에서 빼서 0보다 같거나 작으면 닿지 않는 거리는 없다.
    distance.append(n - (stations[-1] + w))

    # 4. distance를 순회하면서 계산
    for d in distance:
        # 닿지 않으면 스킵
        if d <= 0: continue
        count += math.ceil(d / ((w*2)+1))

    return count

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
