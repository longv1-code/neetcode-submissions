class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        dp[i] = by reaching ith house, i either have robbed the house i - 2 away and decide to rob ith house 
        or skipped it and take what i had at house i - 1
        '''
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        
        return dp[-1]