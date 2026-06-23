class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        pick = [False] * len(nums)

        def backtrack(pick):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    subset.append(nums[i])
                    pick[i] = True
                    backtrack(pick)
                    subset.pop()
                    pick[i] = False
        
        backtrack(pick)
        return res