class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
                board[r][c] = 'T'
                dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in dirc:
                    row, col = r + dr, c + dc
                    dfs(row, col)
        
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)

        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        