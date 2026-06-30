class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Return max dp[i]
        Two choices: skip or rob the neighbor 
        '''

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]

        for i in range(3, len(nums) + 1):
            dp[i] = max(dp[i - 3], dp[i - 2]) + nums[i - 1]
        
        return max(dp)