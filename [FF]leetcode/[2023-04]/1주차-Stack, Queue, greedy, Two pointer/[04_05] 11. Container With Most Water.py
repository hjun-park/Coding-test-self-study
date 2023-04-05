from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        area = 0
        while left < right:
            # 1. area 기존값 vs 가로 x min(둘 중 낮은 세로)
            area = max(area, (right - left) * min(height[left], height[right]))

            # 2. 높이가 낮은 쪽이 한 칸 이동 (높으면 굳이 움직일 필요 없음)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(s.maxArea([1, 1]))  # 1
