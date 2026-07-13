class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {n : True}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                k = len(word)

                if i + k <= n and s[i:i + k] == word:
                    if dfs(i + k):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        
        return dfs(0)