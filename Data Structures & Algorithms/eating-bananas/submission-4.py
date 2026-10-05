# k max -> max(piles)
# k min

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        best = max(piles)
        while l <= r:
            k = (l + r) // 2

            h_now = sum([ -(x // -k) for x in piles ])
            if h_now > h:
                l = k + 1
            elif h_now <= h:
                best = min(k, best)
                r = k - 1


        return best