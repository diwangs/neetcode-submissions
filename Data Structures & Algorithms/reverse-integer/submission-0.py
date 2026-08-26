class Solution:
    def reverse(self, x: int) -> int:
        max32 = 0x7FFFFFFF
        min32 = -max32 - 1

        res = 0
        while x:
            if res > max32 // 10:
                return 0
            if res < min32 // 10:
                return 0

            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            res = (res * 10) + digit

        return res