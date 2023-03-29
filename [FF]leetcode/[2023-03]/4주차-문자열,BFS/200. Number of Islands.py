from collections import deque
from typing import List

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, M = 0, 0


def bfs(grid, a, b):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == '1':
                    q.append((nx, ny))
                    grid[nx][ny] = 0


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global N, M

        N, M = len(grid), len(grid[0])

        count = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    bfs(grid, i, j)
                    count += 1

        return count


s = Solution()
print(s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))  # 1

print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))  # 3
