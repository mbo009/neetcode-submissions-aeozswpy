# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, depth):
            if not root:
                return depth
            
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)

            if abs(left - right) > 1:
                return float('inf')
            
            return max(left, right)

        return dfs(root, 0) != float('inf')