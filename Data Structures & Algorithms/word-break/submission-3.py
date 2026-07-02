class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def dfs(i):
            if i in memo: # if we already computed the DFS at this index, we just return what we found
                return memo[i]

            for word in wordDict:
                # instead of checking each character, we simply search the whole word
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word: 
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)