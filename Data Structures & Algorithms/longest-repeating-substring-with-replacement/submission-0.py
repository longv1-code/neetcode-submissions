class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Pattern: Longest substring -> Sliding Window
        Approach:
        1. Store res to track our length for longest substring
        2. Use two pointers to iterate through the string and measure the length
        3. Iterate through the string with the right pointer
        4. It'll check with the letter on the left pointer
        5. If they mismatch, then we will decrement k by 1
        6. If k is 0, then we 
        Edge Cases:
        - No empty string
        - Single character
        - Duplicate letters
        - No negative values
        - No maximum constraint
        - k = 0 possible
        '''
        count = {}
        l = 0
        res = 0
        maxf = 0

        for r in range(len(s)): # iterate through string
            count[s[r]] = 1 + count.get(s[r], 0) # counts character
            maxf = max(maxf, count[s[r]]) # keeps track of highest freq of a character

            while (r - l + 1) - maxf > k: # if we found we replaced more characters than k times, shrink window
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1) # updates longest length
        
        return res