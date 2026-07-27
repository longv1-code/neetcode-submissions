class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for num in nums:
            nextDp = set()
            for t in dp:
                if num + t == target:
                    return True
                nextDp.add(num + t)
                nextDp.add(t)
            dp = nextDp

        return False