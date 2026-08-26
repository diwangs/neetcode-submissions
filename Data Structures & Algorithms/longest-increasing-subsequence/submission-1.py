class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Smallest element at whcih LIS of length i ends
        dp = []

        def binarySearch(l, e):
            if len(l) == 1:
                return 0
            
            lo = 0
            hi = len(l) - 1

            while lo <= hi:
                mid = (lo+hi)//2

                if l[mid] < e:
                    lo = mid + 1
                elif l[mid] >= e:
                    if l[mid-1] < e:
                        return mid
                    hi = mid - 1
            return 0

        for num in nums:
            if len(dp) == 0 or dp[-1] < num:
                dp.append(num)
            else:
                idx = binarySearch(dp, num)
                dp[idx] = num
            print(dp)
        
        return len(dp)
            