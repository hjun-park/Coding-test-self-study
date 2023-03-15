import heapq


def solution(A, B):
    hA, hB = [], []
    score = 0

    # 우선순위를 내림차순 정렬하기 위해서 (-1)곱하여 정렬
    # 이렇게 하면 A, B 모두 꺼낼 때 가장 큰 것먼저 나오게 된다.
    for a, b in zip(A, B):
        heapq.heappush(hA, -a)
        heapq.heappush(hB, -b)

    # 둘 중 하나가 끝날 때까지
    while hA and hB:
        popA = heapq.heappop(hA)
        popB = heapq.heappop(hB)

        # B가 더 큰 경우에만 처리
        if -popA < -popB:
            score += 1
        else:  # A가 더 크거나 비긴 경우 다음 비교를 위해 B는 push
            heapq.heappush(hB, popB)    # 이미 위에 (-1) 곱했기 때문에 그대로 집어넣어줘도 된다.

    return score


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
