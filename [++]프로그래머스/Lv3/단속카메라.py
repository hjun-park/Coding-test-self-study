import sys
from collections import deque

input = sys.stdin.readline


# 그리디
# 1) 나가는 시간을 기준으로 정렬한다. (나가는 시간을 기준으로 check 갱신할 예정)
# 2) 정렬 하고 특정 차량의 나가는 시간을 기준으로 삼아서
# 그 다음으로 최대한 다음 차들도 포함되는지 체크하자.

def solution(routes):
    count = 0
    routes.sort(key=lambda x: (x[1], x[0]))

    q = deque(routes)

    check = -30001
    while q:
        en, out = q.popleft()

        # 범위 내에 포함되면 CCTV 설치 할 필요가 없음
        if en <= check <= out:
            continue
        # 포함되지 않으면 지점을 나가는 시점으로 변경, 단속카메라 추가
        else:
            check = out
            count += 1

    return count


print(solution([[-20, -15], [-14, -5], [-15, -10], [-18, -13], [-5, -3]]))
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
