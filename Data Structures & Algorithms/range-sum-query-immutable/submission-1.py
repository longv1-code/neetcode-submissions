class NumArray:

    def __init__(self, nums: List[int]):
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        self.arr = prefix


    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right + 1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)