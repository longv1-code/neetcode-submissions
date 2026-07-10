class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0 : 1, 1 : 1}

        def countWays(n):
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] = countWays(n - 1) + countWays(n - 2)
            return memo[n]
        
        return countWays(n)