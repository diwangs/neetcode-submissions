class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        row_tot = len(matrix)
        col_tot = len(matrix[0])
        visited = set()

        row_cur, col_cur = 0, 0
        row_d, col_d = 0, 1

        while len(result) < row_tot * col_tot:
            result.append(matrix[row_cur][col_cur])
            visited.add((row_cur, col_cur))

            if row_cur + row_d >= row_tot or col_cur + col_d >= col_tot or row_cur + row_d < 0 or col_cur + col_d < 0 or (row_cur + row_d, col_cur + col_d) in visited:
                if col_d > 0:
                    row_d, col_d = 1, 0
                elif row_d > 0:
                    row_d, col_d = 0, -1
                elif col_d < 0:
                    row_d, col_d = -1, 0
                elif row_d < 0:
                    row_d, col_d = 0, 1

            row_cur, col_cur = row_cur + row_d, col_cur + col_d

        return result
