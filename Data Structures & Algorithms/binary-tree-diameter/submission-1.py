# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> tuple: # (maxDiameter, height)
            if not root:
                return (0,0)
            left = helper(root.left)
            right = helper(root.right)
            height = max(left[1], right[1]) + 1
            diam = left[1] + right[1]
            maxDiam = max(diam, left[0], right[0])
            return (maxDiam, height)
        return helper(root)[0]