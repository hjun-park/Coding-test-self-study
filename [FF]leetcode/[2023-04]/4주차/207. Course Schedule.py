from collections import defaultdict
from typing import List

# 참고링크
# 1) https://leetcode.com/problems/course-schedule/solutions/3397439/python-toposort-simple-and-clean-beats-88-98/
# 2) https://leetcode.com/problems/course-schedule/solutions/441722/python-99-time-and-100-space-collection-of-solutions-with-explanation/
# 3) https://leetcode.com/problems/course-schedule/solutions/658379/python-by-dfs-and-cycle-detection-w-graph/
# 4) https://leetcode.com/problems/course-schedule/solutions/368508/python3-breadth-first-search-for-cycle-detection/


class Solution:
    # 1. 필요 변수 선언
    visited = []
    graph = defaultdict(list)

    def dfs(self, start, end):
        # 1. (base condition) 만약 가려던 곳을 이미 갔다면
        if self.visited[end]:
            # 1. 시작지와 다음 도착지가 같다면 사이클
            if start == end:
                return False

        # 2. 방문처리
        self.visited[start] = True

        # 3. 현재 상태에서 갈 수 있는 곳들을 순차적으로 돈다.
        for v in self.graph[end]:
            # 1. DFS 순회
            if self.dfs(start, v):
                return False

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 수강과목이 하나인 경우 true
        if numCourses <= 1 or len(prerequisites) == 0:
            return True

        # 2. 수강표를 따라감
        for p in prerequisites:
            v, w = p
            # 1. w를 먼저 들어야만 v를 들을 수 있다.
            self.graph[w].append(v)

        # 3. visited 배열 생성
        self.visited = [False] * numCourses

        # 4. numCourses 개수만큼 dfs 순회
        for n in range(numCourses):
            if self.dfs(n, n):
                return True

        # 5. 다 순회한 경우 사이클이 없다는 것을 의미
        return False


s = Solution()
# print(s.canFinish(2, [[1, 0]]))  # true
# print(s.canFinish(2, [[1, 0], [0, 1]]))  # false
# print(s.canFinish(4, [[3, 2], [1, 0]]))  # true
# print(s.canFinish(4, [[3, 1], [0, 2]]))  # true
# print(s.canFinish(1, []))  # true
print(s.canFinish(2, [[1, 0]]))  # true
