class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        dp[i] = ?
        constraint: circular array, may need to use mod or somehow check if im getting last element, i shouldn't have gotten the first element
        same logic with a little workaround
        last element cannot rely on first element and is forced to skip
        either you use the first or last element
        '''
        n = len(nums)
        res = 0
        if n == 1:
            return nums[0]
        if n == 2 or n == 3:
            return max(nums)

        firstDp = [0] * (n + 1)
        firstDp[1] = nums[0]
        firstDp[2] = nums[1]

        lastDp = [0] * (n + 1)
        lastDp[2] = nums[1]

        for i in range(3, n + 1):
            if i < n:
                firstDp[i] = max(firstDp[i - 2], firstDp[i - 3]) + nums[i - 1]
            lastDp[i] = max(lastDp[i - 2], lastDp[i - 3]) + nums[i - 1]
            res = max(res, firstDp[i], lastDp[i])

        return res