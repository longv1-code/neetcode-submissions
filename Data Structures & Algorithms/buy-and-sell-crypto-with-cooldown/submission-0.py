class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Pattern: Fibonacci Numbers or 0/1 Knapsack
        dp[i][capacity] = reachable(?)
        i is # of coins in consideration

        stuck: confused on what to even set up
        if i buy the first price (1), then i have to select which price greater than (1) to sell for profit, and repeat
        what is the base case?
        find maximum profit after all coins in consideration
        '''

        dp = {} # key: (i, buying), value: max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        
        return dfs(0, True)