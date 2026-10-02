from bisect import bisect_left
class Solution:
    def lengthOfLIS2D(self, nums: List[int]) -> int:
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

    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [ nums[0] ]

        for i in range(1, len(nums)):
            if memo[-1] < nums[i]:
                memo.append(nums[i])
                continue

            idx = bisect_left(memo, nums[i])
            memo[idx] = nums[i]

        return len(memo)