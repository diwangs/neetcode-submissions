# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxSeen):
            nonlocal count
            
            if not node:
                return

            if node.val >= maxSeen:
                count += 1
                maxSeen = node.val

            if node.left:
                dfs(node.left, maxSeen)
            if node.right:
                dfs(node.right, maxSeen)

        dfs(root, float("-inf"))
        return count