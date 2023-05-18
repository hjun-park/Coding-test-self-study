# binary search

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)

        def binary_search(arr, mark, start, end):
            while start <= end:
                mid = (start + end) // 2

                if arr[mid] == mark:
                    return arr[mid]

                # 중간점이 내가 찾는 값보다 더 크다면 -> end를 줄임
                elif arr[mid] > mark:
                    end = mid - 1

                # 내가 찾는 값이 더 크다면 -> start 증가
                else:
                    start = mid + 1

            return -1

        result = binary_search(sorted_nums, target, 0, len(nums) - 1)
        return result if result == -1 else nums.index(result)


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(s.search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 25))  # 4
