"""
Intuition:
- Median is element that splits a sorted list into two equal-sized halves, call them `lo` and `hi`
- `nums1` and `nums2` contributes to `lo` and `hi`, the partition in each list is called `p1` and `p2`
    - `p1` splits `nums1` into `lo1` and `hi1`
- `len(lo) == len(lo1) + len(lo2)`, therefore as `p1` increases, `p2` decreases
- Correct partition is where all elements in `lo1` and `lo2` is smaller than `hi1` and `hi2`
    - This could be simplified by checking the border value only (i.e., highest in `lo1` and lowest in `hi1`)
    - Needs to be true across sublist -> `lo1 <= hi2` and `lo2 <= hi1`
- To find this partition, binary search the partition from one of the sublist (derive the other partition)
    - If `lo1` is too high, decrease `r`
    - If `hi1` is too low, increase `l`

Edge cases:
- 

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Make sure nums1 is the shorter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        tot_len = len(nums1) + len(nums2)

        # Binary search of nums1
        l, r = -1, len(nums1) - 1
        while l <= r:
            p1 = (l + r) // 2
            p2 = (tot_len // 2) - p1 - 2 # -2 from -1 offset from each list

            lo1 = nums1[p1] if p1 >= 0 else float("-inf")
            lo2 = nums2[p2] if p2 >= 0 else float("-inf")
            hi1 = nums1[p1 + 1] if (p1 + 1) < len(nums1) else float("inf")
            hi2 = nums2[p2 + 1] if (p2 + 1) < len(nums2) else float("inf")

            # correct partition
            if lo1 <= hi2 and lo2 <= hi1:
                if tot_len % 2: # odd
                    return min(hi1, hi2)
                else:
                    return (max(lo1, lo2) + min(hi1, hi2)) / 2
            # wrong partition: value from lo1 is too high
            elif lo1 > hi2:
                r = p1 - 1
            # wrong partition: value from hi1 is too low
            elif hi1 < lo2:
                l = p1 + 1
