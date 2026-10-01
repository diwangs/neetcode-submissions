class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [ [ -1 ] * (len(nums) + 1) ] * len(nums)

        def dfs(i: int, j: int) -> int:
            if i == len(nums):
                return 0

            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            memo[i][j + 1] = dfs(i + 1, j) # exclude

            if j == -1 or nums[j] < nums[i]:
                memo[i][j + 1] = max(memo[i][j + 1], 1 + dfs(i + 1, i)) # include

            return memo[i][j + 1]

        return dfs(0, -1)