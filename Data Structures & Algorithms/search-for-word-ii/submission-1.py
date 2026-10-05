"""
Intuition:
- Backtracking from every tile, but cut short with a trie

Complexity:
- The graph DFS part is `3^t` since the word could extend to 3 directions (the fourth is the source, excluded)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Add words to trie
        for word in words:
            n = root
            for char in word:
                if not char in n.children:
                    n.children[char] = TrieNode()
                n = n.children[char]
            n.eow = True

        # DFS
        result = set()
        visited = set()
        def dfs(row: int, col: int, n: TrieNode, prefix: str) -> None:
            nonlocal result

            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] not in n.children or (row, col) in visited:
                return

            n_next = n.children[board[row][col]]
            prefix_next = prefix + board[row][col]
            visited.add((row,col))

            if n_next.eow:
                result.add(prefix_next)

            dfs(row + 1, col, n_next, prefix_next)
            dfs(row, col + 1, n_next, prefix_next)
            dfs(row - 1, col, n_next, prefix_next)
            dfs(row, col - 1, n_next, prefix_next)

            visited.remove((row,col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, '')

        return list(result)


            