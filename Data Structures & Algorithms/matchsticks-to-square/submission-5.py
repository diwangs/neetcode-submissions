class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        line = sum(matchsticks)

        if line % 4:
            return False

        if any(filter(lambda x: x > line // 4, matchsticks)):
            return False

        sides = [0] * 4

        # Optimization: greedy, try largest first
        matchsticks.sort(reverse=True)
        def dfs(i):
            # Base: all matchsticks are placed
            if i == len(matchsticks):
                return True

            for s in range(4):
                # Optimization: skip recursing if one side is overflowing
                if sides[s] + matchsticks[i] > line // 4:
                    continue 

                sides[s] += matchsticks[i]

                if dfs(i+1):
                    return True

                sides[s] -= matchsticks[i]

                # Optimization: skip future empty side after backtracking
                # Idea: "we tried putting it on a previously empty side, and that entire branch failed"
                if sides[s] == 0:
                    break

            return False

        return dfs(0)