class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(r: int, c: int) -> int:
            nonlocal memo

            if (r,c) in memo:
                return memo[(r,c)]

            if r == m - 1:
                memo[(r,c)] = 1
                # return memo[(r,c)]
            elif c == n - 1:
                memo[(r,c)] = 1
                # return memo[(r,c)]
            else:
                memo[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            
            return memo[(r,c)]

        return dfs(0,0)
