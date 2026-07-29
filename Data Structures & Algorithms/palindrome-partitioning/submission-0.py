class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def check_palindrome(s):
            if len(s) == 1:
                return True

            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def backtrack(i):
            if i == len(s):
                res.append(subset.copy())

            temp = ""
            for j in range(i, len(s)):
                temp += s[j]
                if check_palindrome(temp):
                    subset.append(temp)
                    backtrack(j + 1)
                    subset.pop()

        backtrack(0)
        return res