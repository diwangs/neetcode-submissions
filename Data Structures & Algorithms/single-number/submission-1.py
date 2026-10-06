class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniq = 0
        for num in nums:
            uniq ^= num

        return uniq