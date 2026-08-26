class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == -1:
                val = 0
            elif i == 0:
                val = nums[i]
            else:
                val = max(nums[i] + dfs(i-2), dfs(i-1))

            memo[i] = val

            return val

        return dfs(len(nums) - 1)