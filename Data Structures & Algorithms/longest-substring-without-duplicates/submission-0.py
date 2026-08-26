class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        seen = set()
        maxBuff = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[r])
            if maxBuff < r - i + 1:
                maxBuff += 1

        return maxBuff

