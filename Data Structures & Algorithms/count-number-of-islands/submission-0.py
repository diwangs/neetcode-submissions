class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        
        def isInGrid(i, j):
            return i >= 0 and i < n and j >= 0 and j < m 

        def dfs(i, j):
            grid[i][j] = "0"

            for y, x in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if isInGrid(y, x) and grid[y][x] == "1":
                    dfs(y, x)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count



    