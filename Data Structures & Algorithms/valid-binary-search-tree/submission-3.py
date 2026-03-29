# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.prev = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if root.val <= self.prev:
            return False
        self.prev = root.val

        return self.isValidBST(root.right)
# Optimal solution: we should check for left if it's smaller than prev, for right if it's bigger.
# Return AND from all recursion, where True -> valid tree
