class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = abs(x)
        res = int(str(x)[::-1])
        if org < 0:
            res *= -1
        
        if -2**31 <= res <= 2**31:
            return res
        else:
            return 0