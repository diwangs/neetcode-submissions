class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = 0
        globalMax = nums[0]

        for num in nums:
            localMax = max(localMax + num, num)
            globalMax = max(localMax, globalMax)

        return globalMax