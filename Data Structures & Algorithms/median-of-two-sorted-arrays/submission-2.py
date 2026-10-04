class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Make sure nums1 is the shorter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        tot_len = len(nums1) + len(nums2)

        # Binary search of nums1
        l, r = 0, len(nums1) - 1
        while True:
            p1 = (l + r) // 2
            p2 = (tot_len // 2) - p1 - 2

            lo_1 = nums1[p1] if p1 >= 0 else float("-inf")
            lo_2 = nums2[p2] if p2 >= 0 else float("-inf")
            hi_1 = nums1[p1 + 1] if (p1 + 1) < len(nums1) else float("inf")
            hi_2 = nums2[p2 + 1] if (p2 + 1) < len(nums2) else float("inf")

            # correct partition
            if lo_1 <= hi_2 and lo_2 <= hi_1:
                if tot_len % 2: # odd
                    return min(hi_1, hi_2)
                else:
                    return (max(lo_1, lo_2) + min(hi_1, hi_2)) / 2
            # wrong partition: value from lo is larger
            elif lo_1 > hi_2:
                r = p1 - 1
            # wrong partition: 
            else:
                l = p1 + 1
