class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        line = sum(matchsticks)

        if line % 4:
            return False

        if any(filter(lambda x: x > line // 4, matchsticks)):
            return False

        sides = [0] * 4


        matchsticks.sort(reverse=True)
        def dfs(i):
            # All matchsticks are placed
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for s in range(4):
                # Optimization: skip recursing if one side is overflowing
                if sides[s] + matchsticks[i] > line // 4:
                    continue 

                sides[s] += matchsticks[i]

                if dfs(i+1):
                    return True

                sides[s] -= matchsticks[i]

                if sides[s] == 0:
                    break

            return False

        return dfs(0)