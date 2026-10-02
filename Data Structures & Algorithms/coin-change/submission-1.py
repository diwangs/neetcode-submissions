# Note: Knapsack

class Solution:
    def coinChangeBacktrack(self, coins: List[int], amount: int) -> int:
        coins.sort()
        result = -1
        cur_result = 0
        
        def dfs(start: int, remaining: int) -> None:
            nonlocal cur_result, result
            
            if remaining == 0: 
                if result == -1 or cur_result < result:
                    result = cur_result
                return

            for i in range(start, len(coins)):
                if coins[i] > remaining:
                    break
                
                cur_result += 1
                dfs(i, remaining - coins[i])
                cur_result -= 1

        dfs(0, amount)

        return result

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(remaining: int) -> int:
            nonlocal memo
            
            if remaining == 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            result = float("inf")
            for coin in coins:
                if remaining - coin >= 0:
                    result = min(result, 1 + dfs(remaining - coin))

            memo[remaining] = result

            return memo[remaining]

        result = dfs(amount)
        return -1 if result == float("inf") else result
                    

            
