class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(x):
            count = 0
            while x > 0:
                count += x & 1
                x = x >> 1
            return count
        return [countBit(x) for x in range(n+1)]