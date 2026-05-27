class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 0
                area = 1
                for dr, dc in directions:
                    area += dfs(r + dr, c + dc)
                return area
            else:
                return 0
        
        for row in range(m):
            for col in range(n):
                maxArea = max(maxArea, dfs(row, col))
        
        return maxArea