from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[m + n + 1] = nums1[m]
                m -= 1
            else:
                nums1[m + n + 1] = nums2[n]
                n -= 1

        if n >= 0:
            nums1[:n+1] = nums2[:n+1]


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
Solution().merge([1], 1, [], 0)
Solution().merge([0], 0, [1], 1)
