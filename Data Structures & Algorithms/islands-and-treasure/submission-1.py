class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        def bfs(row, col, known_distance):
            nonlocal q
            nonlocal grid

            if grid[row][col] != 0 and grid[row][col] <= known_distance:
                return
            
            grid[row][col] = known_distance

            if row - 1 >= 0 and grid[row-1][col] > known_distance + 1:
                q.append((row-1, col, known_distance + 1))
            if col - 1 >= 0 and grid[row][col-1] > known_distance + 1:
                q.append((row, col-1, known_distance + 1))
            if row + 1 < len(grid) and grid[row+1][col] > known_distance + 1:
                q.append((row+1, col, known_distance + 1))
            if col + 1 < len(grid[0]) and grid[row][col+1] > known_distance + 1:
                q.append((row, col+1, known_distance + 1))

        for cur_row in range(len(grid)):
            for cur_col in range(len(grid[0])):
                if grid[cur_row][cur_col] == 0:
                    q.append((cur_row, cur_col, 0))

        while q:
            bfs(*q.popleft())