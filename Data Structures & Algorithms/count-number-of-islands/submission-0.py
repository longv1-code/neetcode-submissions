class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            dirc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dr, dc in dirc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    dfs(nr, nc)
            

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1

        return res