class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ''
        
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1

                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
        
        for i in range(n):
            for j in range(n):
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
        
        return res