class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                memo[i] = nums[i]
            elif i == len(nums)-2:
                memo[i] = max(memo[i+1], nums[i])
            else:
                memo[i] = max(memo[i+1], nums[i] + memo[i+2])

        return memo[0]