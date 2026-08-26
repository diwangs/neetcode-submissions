class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxBuff = 0
        queue = []

        def isInGrid(i, j):
            return i >= 0 and i < n and j >= 0 and j < m

        def bfs(i, j, depth):
            nonlocal maxBuff
            grid[i][j] = 2

            for y, x in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if isInGrid(y, x) and grid[y][x] == 1:
                    queue.append((y, x, depth + 1))
            
            if depth > maxBuff:
                maxBuff = depth

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while len(queue) > 0:
            bfs(*queue.pop(0))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return maxBuff 
                    
