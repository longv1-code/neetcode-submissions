class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(summ, start):
            if summ > target:
                return
            elif summ == target:
                res.append(subset.copy())
            
            for i in range(start, len(nums)):
                summ += nums[i]
                subset.append(nums[i])
                backtrack(summ, i)
                summ -= nums[i]
                subset.pop()
            start += 1
        
        backtrack(0, 0)
        return res