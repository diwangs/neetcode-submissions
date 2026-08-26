class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask32 = 0xFFFFFFFF
        int32max = 0x7FFFFFFF

        while b:
            a = (a ^ b) & mask32
            b = (((a ^ b) & b) << 1) & mask32
        
        return a if a <= int32max else ~(a ^ mask32)

        