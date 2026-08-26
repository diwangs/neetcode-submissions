class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        # Given row, col that's 1, explore its neighbor
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            grid[row][col] = "0"

            while q:
                row_cur, col_cur = q.popleft()
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nr, nc = row_cur + dr, col_cur + dc

                    # Check bound
                    if (nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == "0"):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands



