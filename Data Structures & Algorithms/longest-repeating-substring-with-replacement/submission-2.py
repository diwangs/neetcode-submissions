"""
Intuition:
- Convert to the most frequent in a substring

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        freq = {}

        i = 0
        j = 0
        while j < len(s):
            freq[s[j]] = freq.get(s[j], 0) + 1
            j += 1

            # Keep validity
            most_freq = max(list(freq.values())) if freq else 0
            while j - i - most_freq > k:
                freq[s[i]] -= 1
                i += 1

            result = max(result, j-i)
            

        return result

        