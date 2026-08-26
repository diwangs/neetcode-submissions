class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        
        hi = maxPile
        lo = 1

        result = hi
        
        while lo <= hi:
            k = (lo + hi) // 2
            spent = sum([-(x // -k) for x in piles])

            if spent <= h:
                result = k
                hi = k - 1
            else:
                lo = k + 1

        return result
        