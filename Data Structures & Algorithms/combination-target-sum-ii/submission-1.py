class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        path = []
        result = []

        def dfs(start: int, residue: int) -> None:
            # Base
            if residue == 0:
                result.append(path[:])
                return

            i = start
            last = None
            while i < len(candidates):
                if last and candidates[i] == last:
                    i += 1
                    continue
                
                if candidates[i] > residue:
                    break

                path.append(candidates[i])
                dfs(i + 1, residue - candidates[i])
                path.pop()

                last = candidates[i]

        dfs(0, target)

        return result