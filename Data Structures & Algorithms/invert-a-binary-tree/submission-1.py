# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(n: TreeNode) -> TreeNode:
            if not n.left and not n.right:
                return n

            if n.left:
                n.left = invert(n.left)

            if n.right:
                n.right = invert(n.right)

            temp = n.left
            n.left = n.right
            n.right = temp

            return n

        if not root:
            return root
        
        return invert(root)