class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque

        m, n = len(heights), len(heights[0])
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

        def bfs(start):
            q = deque(start)
            dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            seen = set(start)
            while q:
                r, c = q.popleft()
                for dr, dc in dirc:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and heights[r][c] <= heights[nr][nc] and (nr, nc) not in seen:
                        q.append([nr, nc])
                        start.append([nr, nc])
                        seen.add((nr, nc))

            return seen     

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r in range(m) for c in range(n) if (r, c) in pacific if (r, c) in atlantic]