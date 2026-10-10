class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def count(s: str) -> dict:
            result = {}
            for c in s:
                result[c] = result.get(c, 0) + 1
            return result
        
        s1_charset = count(s1)

        i = 0
        for j in range(len(s2)+1):       
            if j - i < len(s1):
                continue

            print(s2[i:j])
            if s1_charset == count(s2[i:j]):
                return True

            i += 1

        return False