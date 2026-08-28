class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        curArea = 0

        def bfs(row, col):
            nonlocal curArea
            q = deque()
            q.append((row, col))
            grid[row][col] = 0

            while q:
                cur_row, cur_col = q.popleft()
                curArea = curArea + 1

                for d_row, d_col in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_row, next_col = cur_row + d_row, cur_col + d_col

                    if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]) or grid[next_row][next_col] == 0:
                        continue

                    q.append((next_row, next_col))
                    grid[next_row][next_col] = 0


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    bfs(row, col)
                    if maxArea < curArea:
                        maxArea = curArea
                    curArea = 0

        return maxArea