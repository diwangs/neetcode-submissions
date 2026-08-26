class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutationBuffer = []

        def dfs(rest):
            if len(rest) == 0:
                result.append(permutationBuffer.copy())
                return

            for i in range(len(rest)):
                chosen = rest.pop(0)
                permutationBuffer.append(chosen)
                dfs(rest)
                permutationBuffer.pop()
                rest.append(chosen)
            
        dfs(nums)
        return result