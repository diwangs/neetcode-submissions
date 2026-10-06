class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in num_set:
                seq_len = 1
                while num + seq_len in num_set:
                    seq_len += 1
                result = max(result, seq_len)

        return result