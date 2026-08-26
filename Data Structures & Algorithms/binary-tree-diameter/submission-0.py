# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Either:
# - Depth
# - maxDepth of left + maxDepth of right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):
            if not root:
                return 0
            return 1 + max([maxDepth(root.left), maxDepth(root.right)])
        
        if not root:
            return 0
        
        return max([maxDepth(root.left) + maxDepth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)])