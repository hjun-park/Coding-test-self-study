from collections import deque
from typing import List


# DFS
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        n, m = len(matrix), len(matrix[0])
        _max = -1

        def bfs(a, b):
            cnt = 1
            q = deque()
            q.append((a, b, cnt))

            while q:
                x, y, cnt = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    if 0 <= nx < n and 0 <= ny < m:
                        if matrix[x][y] < matrix[nx][ny]:
                            q.append((nx, ny, cnt + 1))

            return cnt

        for i in range(n):
            for j in range(m):
                _max = max(bfs(i, j), _max)

        return _max


s = Solution()
# print(s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))  # 4   (1, 2, 6, 9)
# print(s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))  # 4   (3, 4, 5, 6)
print(s.longestIncreasingPath(
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
     [39, 38, 37, 36, 35, 34, 33, 32, 31, 30], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
     [59, 58, 57, 56, 55, 54, 53, 52, 51, 50], [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
     [79, 78, 77, 76, 75, 74, 73, 72, 71, 70], [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
     [99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
     [119, 118, 117, 116, 115, 114, 113, 112, 111, 110], [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
     [139, 138, 137, 136, 135, 134, 133, 132, 131, 130], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
