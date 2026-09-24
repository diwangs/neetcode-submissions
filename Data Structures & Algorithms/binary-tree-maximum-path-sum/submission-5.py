# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def traverse(n: TreeNode) -> int:
            nonlocal result

            # Calculate maximum value of only-one leg
            path_max = n.val

            if n.left:
                left_max = traverse(n.left)

                if n.val + left_max > path_max:
                    path_max = n.val + left_max

            if n.right:
                right_max = traverse(n.right)

                if n.val + right_max > path_max:
                    path_max = n.val + right_max

            # Scenario 1: arch
            arch_max = n.val
            if n.left:
                arch_max += left_max
            if n.right:
                arch_max += right_max

            if path_max > arch_max:
                arch_max = path_max
            
            if arch_max > result:
                result = arch_max

            # Scenario 2: non-arch
            return path_max

        traverse(root)

        return result

        