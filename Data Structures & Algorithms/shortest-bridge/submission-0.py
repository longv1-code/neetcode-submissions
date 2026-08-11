class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        direc = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            
            for dr, dc in direc:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    dfs(nr, nc)

        def bfs():
            res, q = 0, deque(visited)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direc:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                            if grid[nr][nc] == 1:
                                return res
                            q.append((nr, nc))
                            visited.add((nr, nc))

                res += 1

        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()