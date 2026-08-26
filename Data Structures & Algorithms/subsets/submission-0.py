class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subsetBuff = []
        
        def dfs(i):
            # no need to do nonlocal for list

            # If we have considered all elements
            if not i < len(nums):
                result.append(subsetBuff.copy())
                return

            # Decision to include nums[i]
            subsetBuff.append(nums[i])
            dfs(i + 1)

            # Backtrack the buffer, exclude nums[i]
            subsetBuff.pop()
            dfs(i + 1)

        dfs(0)
        return result