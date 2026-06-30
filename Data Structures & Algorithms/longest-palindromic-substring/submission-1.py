class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        if we find one palindrome, we save their indices
        if we find another with those indices inside, then we just expand since it's guarenteed 

        how do you start finding the palindrome?
        dp[i] = substring that ends here or start a new one
        if end here, is it a palindrome? if so, is there an existing a palindrome before it to extend?
        if not, we start new

        how to keep track of past palindromes and to know which one to extend?
        '''
        resLen = 0
        res = ''

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        return res