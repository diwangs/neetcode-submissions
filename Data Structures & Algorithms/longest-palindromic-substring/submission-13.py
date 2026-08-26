class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = {}
        maxLen = 0
        maxI = 0

        def dfs(i, j):
            if j < i:
                return False

            nonlocal maxLen, maxI

            if (i, j) in dp:
                return dp[i, j]
            val = False

            curLen = j + 1 - i
            if (curLen <= 2 or dfs(i+1, j-1)) and s[i] == s[j]:
                val = True
                if maxLen < curLen:
                    maxLen = curLen
                    maxI = i
            dfs(i+1,j)
            dfs(i,j-1)

            if (i, j) not in dp:
                dp[i, j] = val
            return val

        dfs(0, n-1)
        return s[maxI: maxI + maxLen]

                    