class Solution:
    def reverse(self, x: int) -> int:
        max32 = 0x7FFFFFFF
        min32 = -max32 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            res = (res * 10) + digit

            if res > max32:
                return 0
            if res < min32:
                return 0

        return res