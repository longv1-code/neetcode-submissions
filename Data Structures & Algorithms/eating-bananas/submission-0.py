class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        L, R = 1, max(piles)
        from math import ceil

        while L <= R:
            k = (L + R) // 2
            totalTime = 0

            for x in piles:
                totalTime += ceil(x / k)
            
            if totalTime <= h:
                res = k
                R = k - 1
            else:
                L = k + 1
        
        return res