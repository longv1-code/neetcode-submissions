class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res, inc, dec = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                inc, dec = 1, 1
            elif nums[i - 1] < nums[i]:
                inc, dec, = inc + 1, 1
            else:
                inc, dec = 1, dec + 1
            
            res = max(res, inc, dec)
        
        return res