class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            grid[r][c] = '0'
            dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in dirc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    dfs(nr, nc)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    islands += 1
        
        return islands