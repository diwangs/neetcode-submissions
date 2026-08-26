class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceSet = {}
        for i in range(len(nums)):
            if target - nums[i] in differenceSet:
                return [differenceSet[target - nums[i]], i]    
            differenceSet[nums[i]] = i
            
            
    