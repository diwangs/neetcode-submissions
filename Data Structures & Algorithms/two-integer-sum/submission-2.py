class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = { v: k for k, v in enumerate(nums)}

        for i in range(len(nums)):
            num = nums[i]
            if target - num in idx_map and i != idx_map[target-num]:
                return [i, idx_map[target - num]]
        