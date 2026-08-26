class Solution:
    def reverseBits(self, n: int) -> int:
        after = 0
        for i in range(32):
            after |= ((n >> i) & 1) << (31 - i)
        return after