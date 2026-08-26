class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1st step: find cut
        loCut = 0
        hiCut = len(nums) - 1
        res = loCut

        while loCut <= hiCut:
            midCut = (loCut + hiCut) // 2

            if nums[0] <= nums[midCut]:
                res = midCut
                loCut = midCut + 1
            else:
                hiCut = midCut - 1

        # 2nd step: actual binary search
        lo = 0
        hi = len(nums) - 1
        if target >= nums[0] and target <= nums[res]:
            hi = res
        else: 
            lo = res + 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return mid

        return -1



        