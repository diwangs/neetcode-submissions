# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nthSmallest = 0
        val = root.val
        
        def dfs(node):
            nonlocal nthSmallest, val

            if not node:
                return

            if node.left:
                dfs(node.left)

            nthSmallest += 1

            if nthSmallest == k:
                val = node.val
                return

            if node.right:
                dfs(node.right)

        dfs(root)
        return val