from collections import defaultdict, deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        _len = len(isConnected)
        visited = [0] * _len
        graph = defaultdict(list)

        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 1

            while q:
                v = q.popleft()

                for n in graph[v]:
                    if not visited[n]:
                        q.append(n)
                        visited[n] = 1

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j]:
                    graph[i].append(j)

        cnt = 0
        for i in range(_len):
            if not visited[i]:
                bfs(i)
                cnt += 1

        return cnt


s = Solution()
# print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
# print(s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
print(s.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))  # 1
