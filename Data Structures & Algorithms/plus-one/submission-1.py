class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
            i -= 1

        return [1] + digits
