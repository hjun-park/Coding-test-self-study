from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> str:
        h = len(nums) - len(set(nums))
        nums_set = str(list(set(nums)))[:-1].replace(' ', '')

        a = ','.join(['_' for _ in range(h)])
        return f'{str(len(set(nums)))}, nums = {nums_set},{a}]'


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
