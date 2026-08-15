class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            dp[i][n] = m - i
        for i in range(n):
            dp[m][i] = n - i

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
        
        return dp[0][0]