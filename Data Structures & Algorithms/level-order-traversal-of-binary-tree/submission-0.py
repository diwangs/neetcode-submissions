# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def traverse(n: TreeNode, level: int) -> None:
            nonlocal result

            if len(result) <= level:
                result.append([n.val])
            else:
                result[level].append(n.val)

            if n.left:
                traverse(n.left, level + 1)

            if n.right:
                traverse(n.right, level + 1)

        if root:
            traverse(root, 0)

        return result

