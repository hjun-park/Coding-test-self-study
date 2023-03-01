import sys
from typing import List

input = sys.stdin.readline


# 이진탐색 문제

class Solution:
    # 바나나를 h 시간 내로 다 먹을 수 있는지 ?
    def possible(self, piles, k, h):
        total = 0
        for p in piles:
            total += p // k if p % k == 0 else p // k + 1

        if total <= h:
            return True
        else:
            return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1) 바나나 전체와 시간을 나눈 값이 mid
        # max : max(piles), min = 1
        start, end = 1, max(piles)

        while start <= end:
            mid = (start + end) // 2

            # 바나나를 먹을 수 있는 경우 (mid가 많음)
            if self.possible(piles, mid, h):
                end = mid - 1
            else:
                start = mid + 1

        return start


print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6))
