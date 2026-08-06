class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        maxRange = n * n
        seen = set()
        a, b = 0, 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] in seen:
                    a = grid[r][c]
                seen.add(grid[r][c])

        for i in range(1, maxRange + 1):
            if i not in seen:
                b = i

        return [a, b]
