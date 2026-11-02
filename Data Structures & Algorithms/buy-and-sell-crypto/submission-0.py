class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        res = 0
        for price in prices:
            if minPrice > price:
                minPrice = price
            res = max(res, price - minPrice)
        
        return res