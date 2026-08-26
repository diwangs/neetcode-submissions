class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        sumBuff = []

        def dfs(i):
            if sum(sumBuff) >= target:
                if sum(sumBuff) == target:
                    result.append(sumBuff.copy())
                return

            for j in range(i, len(nums)):
                sumBuff.append(nums[j])
                dfs(j)
                sumBuff.pop()

        dfs(0)
        return result