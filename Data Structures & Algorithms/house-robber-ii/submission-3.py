class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def profit(nums):
            n = len(nums)
            dp = [0] * n

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            
            return dp[-1]

        return max(profit(nums[:len(nums) - 1]), profit(nums[1:]))