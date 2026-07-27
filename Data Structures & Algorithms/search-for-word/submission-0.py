class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(idx, r, c):
            if idx == len(word) - 1 and word[idx] == board[r][c]:
                return True
            
            seen.add((r, c))
            dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirc:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == word[idx + 1] and (nr, nc) not in seen:
                    if dfs(idx + 1, nr, nc):
                        return True
            
            seen.remove((r, c))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    seen = set()
                    if dfs(0, i, j):
                        return True

        return False