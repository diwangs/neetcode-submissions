# Lesson:
# - Don't use a set, it's slower than backtracking
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        path = []
        result = []

        def dfs(start: int, remaining: int):
            nonlocal path, result

            # Base
            if remaining == 0:
                result.append(list(path))
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                path.append(nums[i])
                dfs(i, remaining - nums[i])
                path.pop()

        dfs(0, target)

        return result