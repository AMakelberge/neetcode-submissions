# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode]) -> tuple: #(isBalanced, height)
            if not root:
                return (True, 0)
            
            left, right = helper(root.left), helper(root.right)
            if not (left[0] and right[0]):
                return (False, 0)
            if (abs(left[1] - right[1]) <= 1):
                return (True, max(left[1],right[1]) + 1)
            return (False, 0)
        return helper(root)[0]

        