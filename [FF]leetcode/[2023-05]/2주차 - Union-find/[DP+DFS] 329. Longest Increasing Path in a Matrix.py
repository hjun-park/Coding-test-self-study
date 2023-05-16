from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        _max = 0

        def dfs(x, y):
            if dp[x][y] != 0:
                return dp[x][y]

            length = 1
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and matrix[x][y] < matrix[nx][ny]:
                    length = max(length, dfs(nx, ny) + 1)

            dp[x][y] = length
            return length

        for i in range(n):
            for j in range(m):
                _max = max(_max, dfs(i, j))

        return _max
