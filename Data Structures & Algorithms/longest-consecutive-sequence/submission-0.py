class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSeqLength = 0

        # First loop: which number is the start of a sequence?
        for num in nums:
            if num - 1  in numsSet: # O(1)
                continue

            curNum = num
            seqLength = 1
            for i in range(1, len(nums)):
                if curNum + 1 in numsSet:
                    curNum += 1
                    seqLength += 1

            if seqLength > maxSeqLength:
                maxSeqLength = seqLength

        return maxSeqLength



            
        