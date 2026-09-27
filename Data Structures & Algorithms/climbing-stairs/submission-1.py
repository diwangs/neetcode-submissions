class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [ 0 ] * n

        def count_step(start: int) -> int:
            nonlocal memo

            if memo[start] != 0:
                return memo[start]

            # Base
            if start == n - 1:
                memo[start] = 1
            elif start == n - 2:
                memo[start] = 2
            # Recurrence
            else:
                memo[start] = count_step(start+1) + count_step(start+2)

            return memo[start]

        return count_step(0)

            
                