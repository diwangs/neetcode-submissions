# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs1(node1, node2):
            if not node1 or not node2:
                return not node1 and not node2

            return node1.val == node2.val and dfs1(node1.left, node2.left) and dfs1(node1.right, node2.right)

        def dfs2(node1, node2):
            if not node1 or not node2:
                return not node1 and not node2

            return dfs1(node1, node2) or dfs2(node1.left, node2) or dfs2(node1.right, node2)

        return dfs2(root, subRoot)
        