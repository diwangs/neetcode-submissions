class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToAlphaList = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        result = []
        charBuffer = []

        def dfs(i):
            if not i < len(digits):
                if len(charBuffer) > 0:
                    result.append(''.join(charBuffer))
                return

            for char in numToAlphaList[digits[i]]:
                charBuffer.append(char)
                dfs(i + 1)
                charBuffer.pop()

        dfs(0)
        return result