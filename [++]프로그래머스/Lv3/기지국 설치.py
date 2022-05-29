from math import ceil


def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1

    start = 1

    # 설치할 기지국의 왼쪽 파트에서 아파트의 개수를 W만큼 나누어 몇 개 설치할 수 있는지를 answer에 반영
    for s in stations:
        answer += max(ceil((s - w - start) / W), 0)
        start = s + w + 1

    # 마지막 기지국의 오른쪽 파트 공간이 남아있는지 확인 후 남아있다면 기지국을 설치하여 answer에 반영
    if n >= start:
        answer += ceil((n - start + 1) / W)

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
