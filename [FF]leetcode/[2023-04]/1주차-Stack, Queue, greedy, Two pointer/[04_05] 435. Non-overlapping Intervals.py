from typing import List

'''
목표 : 배열 안의 `interval`들이 서로 겹치지 않도록 제거 해야 하는 개수를 최소화 할 것
핵심
 1. `interval`이 큰 경우 즉, [start of i, end of i]에서 (end of i) 기준으로 오름차순 정렬 해야 순차적으로 접근 가능
 
과정
 1. 정렬 (end of i) 오름차순
 2. 맨 처음 값을 cur로 하고 index 1부터 비교 진행
    2-1. 겹치지 않아야 하니까 현재의 끝 값과 `cur[1]` 다음의 처음 값 `next[0]` 비교 ( cur[1] <= next[0] 인 경우만 겹치지 않음)
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #  1. 정렬 x[1]기준
        intervals.sort(key=lambda x: x[1])
        #  2. 맨 처음 값을 cur로 설정
        cur = intervals[0]
        count = 1   # 겹치지 않는 리스트 개수 (처음은 무조건 포함)
        # 3.  index 1부터 비교 진행
        for i in range(1, len(intervals)):
            # 1. 만약 겹치지 않는다면 count 증가
            if cur[1] <= intervals[i][0]:
                count += 1
                cur = intervals[i]     # 2. cur 위치 조정
        return len(intervals) - count


s = Solution()
print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
print(s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))  # 2
print(s.eraseOverlapIntervals([[1, 2], [2, 3]]))  # 0
