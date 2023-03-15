import heapq
import sys
from math import pow

input = sys.stdin.readline


# n : 시간
# works : 작업량
# 1시간 만큼 작업량 1
# 야근 피로도 => 야근 시작한 시점
def solution(n, works):
    hq = []
    for w in works:
        heapq.heappush(hq, w * (-1))

    for i in range(n):
        work = heapq.heappop(hq)
        if work == 0:  # 이미 일을 다 한 경우
            break
        heapq.heappush(hq, work + 1)

    # 제곱해도 음수/양수 구분 안 하니까 계산한다.
    # result = [(x * -1) for x in hq]

    answer = 0
    for num in hq:
        answer += pow(num, 2)

    return int(answer)


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
