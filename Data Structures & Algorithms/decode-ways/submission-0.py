class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        dp[i] = nums of ways to decode if substring ends at i
        '''
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(s) + 1):
            oneDigit = s[i - 1]
            twoDigit = s[i - 2:i]

            if oneDigit != '0':
                dp[i] += dp[i - 1]
            if '10' <= twoDigit <= '26':
                dp[i] += dp[i - 2]
        
        return dp[-1]

        