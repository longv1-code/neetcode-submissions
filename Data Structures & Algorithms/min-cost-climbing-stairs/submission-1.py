class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        dp[i] = minimum cost of i - 1 and i - 2 step + ith step
        dp[0] = cost[0]
        dp[1] = cost[1]
        '''
        dp = [-1] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        def solve(i):
            if dp[i] != -1:
                return dp[i]

            dp[i] = min(solve(i - 2), solve(i - 1)) + cost[i]
            return dp[i]
        
        solve(len(cost) - 1)
        return min(dp[-1], dp[-2])