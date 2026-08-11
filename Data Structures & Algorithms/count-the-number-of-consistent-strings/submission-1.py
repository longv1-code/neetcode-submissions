class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = len(words)
        for word in words:
            for c in word:
                if c not in allowed:
                    res -= 1
                    break
        
        return res