class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(tuple(s))) == ''.join(sorted(tuple(t)))
        