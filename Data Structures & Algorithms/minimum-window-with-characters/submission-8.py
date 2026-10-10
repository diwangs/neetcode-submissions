class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        result = ""

        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        required = len(t_count)

        satisfied = 0 # unique
        s_count = {} # duplicates
        i = j = 0
        while j < len(s):
            s_count[s[j]] = s_count.get(s[j], 0) + 1
            if s[j] in t_count and s_count[s[j]] == t_count[s[j]]:
                satisfied += 1
            j += 1

            while satisfied == required and s_count[s[i]] > t_count.get(s[i], 0):
                s_count[s[i]] -= 1
                i += 1

            # TODO Optimization: track the index and only slice at the end
            if satisfied == required:
                result = s[i:j] if not result or j-i < len(result) else result

        return result

            

