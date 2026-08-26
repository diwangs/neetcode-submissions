class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        num = n
        while num != 1:
            happiness = 0
            carry = num
            while carry:
                digit = carry % 10
                carry = carry // 10
                happiness += digit ** 2
            
            num = happiness
            if num in seen:
                return False
            seen.add(num)

        return True