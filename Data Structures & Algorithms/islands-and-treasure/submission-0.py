class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        land = 2**31 - 1
        chest = 0
        water = -1

        m, n = len(grid), len(grid[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == chest:
                    q.append((r, c)) 

        while q:
            r, c = q.popleft()
            dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirc:
                row, col = r + dr, c + dc

                if 0 <= row < m and 0 <= col < n and grid[row][col] == land:
                    grid[row][col] = min(grid[r][c] + 1, grid[row][col])
                    q.append((row, col))
        