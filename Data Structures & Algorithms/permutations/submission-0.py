class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                backtrack()
                subset.pop()
        
        backtrack()
        return res