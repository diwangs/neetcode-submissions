class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def dfs(row: int, col: int, suffix: str) -> bool:
            nonlocal visited
            
            if board[row][col] != suffix[0]:
                return False

            suffix = suffix[1:]

            if suffix == "":
                return True

            visited.add((row,col))

            for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                row_next = row + dr
                col_next = col + dc

                if 0 <= row_next < len(board) and 0 <= col_next < len(board[0]) and (row_next,col_next) not in visited:
                    if dfs(row_next, col_next, suffix):
                        return True

            visited.remove((row,col))


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, word):
                    return True

        return False