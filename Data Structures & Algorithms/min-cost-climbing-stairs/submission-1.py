class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * n

        def dfs(start: int) -> int:
            nonlocal memo

            if memo[start] != 0:
                return memo[start]

            if start == n -1 or start == n-2:
                memo[start] = cost[start]
            else:
                memo[start] = cost[start] + min(dfs(start + 1), dfs(start + 2))

            return memo[start]

        return min(dfs(0), dfs(1))
            
        