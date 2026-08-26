class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, isOnCooldown):
            if i >= len(prices):
                return 0

            if (i, isOnCooldown) in dp:
                return dp[i, isOnCooldown]
            
            hold = dfs(i+1, isOnCooldown)
            # buy
            if not isOnCooldown:
                buy = - prices[i] + dfs(i+1, not isOnCooldown) 
                dp[i, isOnCooldown] = max(buy, hold)
            # sell
            else:
                sell = prices[i] + dfs(i+2, not isOnCooldown)
                dp[i, isOnCooldown] = max(sell, hold)

            return dp[i, isOnCooldown]


        return dfs(0, False)