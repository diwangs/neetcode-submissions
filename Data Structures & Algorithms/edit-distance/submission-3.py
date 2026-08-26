class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        
        def dfs(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if (i,j) in dp:
                return dp[i,j]

            if word1[i] == word2[j]:
                forwardCost = 0
            else:
                forwardCost = 1

            deletion = dfs(i-1,j)+1
            addition = dfs(i,j-1)+1
            forward = dfs(i-1,j-1)+forwardCost

            dp[i,j] = min(deletion,addition,forward)

            return dp[i,j]

        return dfs(len(word1)-1,len(word2)-1)
