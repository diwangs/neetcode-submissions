# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, isLargest) -> int:
            if isLargest:
                if not node.right:
                    return node.val
                else:
                    return dfs(node.right, isLargest)
            else:
                if not node.left:
                    return node.val
                else:
                    return dfs(node.left, isLargest)

        if not root:
            return True

        isLeftBST = True
        if root.left:
            isLeftBST = root.val > dfs(root.left, True) and self.isValidBST(root.left)

        isRightBST = True
        if root.right:
            isRightBST = root.val < dfs(root.right, False) and self.isValidBST(root.right)

        return isLeftBST and isRightBST

        